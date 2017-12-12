# coding:utf-8

from setuptools import setup, find_packages


packages = find_packages('typeidea')
print(packages)

setup(
    name='typeidea',
    version='0.1',
    description='Blog System base on Django',
    author='the5fire',
    author_email='thefivefire@gmail.com',
    url='https://www.the5fire.com',
    packages=packages,
    package_dir={'': 'typeidea'},
    include_package_data=True,  # 方法二  ，配置MANIFEST.in文件
    install_requires=[
        'django==1.11.8',
    ],
    scripts=[
        'typeidea/manage.py',
    ],
)
