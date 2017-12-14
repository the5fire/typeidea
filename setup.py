# coding:utf-8

from setuptools import setup, find_packages


packages = find_packages('typeidea')
print(packages)

setup(
    name='typeidea',
    version='0.7',
    description='Blog System base on Django',
    author='the5fire',
    author_email='thefivefire@gmail.com',
    url='https://www.the5fire.com',
    packages=packages,
    package_dir={'': 'typeidea'},
    include_package_data=True,  # 方法二  ，配置MANIFEST.in文件
    install_requires=[
        'django==1.11.8',
        'django-autocomplete-light==3.2.10',
        'hiredis==0.2.0',
        'redis==2.10.6',
        'django-ckeditor==5.3.1',
        'django-debug-toolbar==1.9.1',
        'mysqlclient==1.3.12',
        'Pillow==4.3.0',
        'xadmin==0.6.1',
        'djangorestframework==3.7.3',
        'django-reversion==2.0.10',
        'Markdown==2.6.9',
        'django-redis==4.8.0',
        'coreapi==2.3.3',
        'gunnicorn==19.7.1',
    ],
    scripts=[
        'typeidea/manage.py',
    ],
)
