"""
这是fabric2版本的代码，fabfile1.py中是针对fabric3写的
"""
import os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape
from invoke import task


PROJECT_NAME = 'typeidea'
SETTINGS_BASE = 'typeidea/typeidea/settings/base.py'
DEPLOY_PATH = '/home/the5fire/venvs/typeidea-env'
VENV_ACTIVATE = os.path.join(DEPLOY_PATH, 'bin', 'activate')
PYPI_HOST = '127.0.0.1'
PYPI_INDEX = 'http://127.0.0.1:8080/simple'
PROCESS_COUNT = 2
PORT_PREFIX = 909


@task
def build(c, version=None, bytescode=False):
    """ 本地打包并且上传包到pypi上
        1. 配置版本号
        2. 打包并上传
    Usage:
        fab build --version 1.4
    """
    if not version:
        version = datetime.now().strftime('%m%d%H%M%S')  # 当前时间，月日时分秒

    _version = _Version()
    _version.set(['setup.py', SETTINGS_BASE], version)

    result = c.run('echo $SHELL', hide=True)
    user_shell = result.stdout.strip('\n')
    c.run('python setup.py bdist_wheel upload -r internal', warn=True, shell=user_shell)

    _version.revert()


@task
def deploy(c, version, profile):
    """ 部署指定版本
        1. 确认虚拟环境已经配置
        2. 激活虚拟环境
        3. 安装软件包
        4. 启动

    Usage:
        fab -H myserver -S ssh_config deploy 1.4 product
    """
    _ensure_virtualenv(c)
    package_name = PROJECT_NAME + '==' + version
    with c.prefix('source %s' % VENV_ACTIVATE):
        c.run('pip install %s -i %s --trusted-host %s' % (
            package_name,
            PYPI_INDEX,
            PYPI_HOST,
        ))
        _reload_supervisoird(c, DEPLOY_PATH, profile)


class _Version:
    origin_record = {}

    def replace(self, f, version):
        with open(f, 'r') as fd:
            origin_content = fd.read()
            content = origin_content.replace('${version}', version)

        with open(f, 'w') as fd:
            fd.write(content)

        self.origin_record[f] = origin_content

    def set(self, file_list, version):
        for f in file_list:
            self.replace(f, version)

    def revert(self):
        for f, content in self.origin_record.items():
            with open(f, 'w') as fd:
                fd.write(content)


def _ensure_virtualenv(c):
    if c.run('test -f %s' % VENV_ACTIVATE, warn=True).ok:
        return True

    if c.run('test -f %s' % DEPLOY_PATH, warn=True).failed:
        c.run('mkdir -p %s' % DEPLOY_PATH)

    c.run('python3.6 -m venv %s' % DEPLOY_PATH)
    c.run('mkdir -p %s/tmp' % DEPLOY_PATH)  # 创建tmp目录存放pid和log


def _upload_conf(c, deploy_path, profile):
    env = Environment(
        loader=FileSystemLoader('conf'),
        autoescape=select_autoescape(['.conf'])
    )
    template = env.get_template('supervisord.conf')
    context = {
        'process_count': PROCESS_COUNT,
        'port_prefix': PORT_PREFIX,
        'profile': profile,
        'deploy_path': deploy_path,
    }
    content = template.render(**context)
    tmp_file = '/tmp/supervisord.conf'
    with open(tmp_file, 'wb') as f:
        f.write(content.encode('utf-8'))

    destination = os.path.join(deploy_path, 'supervisord.conf')
    c.put(tmp_file, destination)


def _reload_supervisoird(c, deploy_path, profile):
    _upload_conf(c, deploy_path, profile)
    c.run('supervisorctl -c %s/supervisord.conf shutdown' % deploy_path, warn=True)
    c.run('supervisord -c %s/supervisord.conf' % deploy_path)
