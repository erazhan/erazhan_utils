# -*- coding = utf-8 -*-
# @time: 2022/2/18 5:52 下午
# @Author: erazhan
# @File: setup.py

# ----------------------------------------------------------------------------------------------------------------------
from setuptools import setup, find_packages

setup(
    name = "erazhan_utils",
    version = "0.0.7",  # 暂时在__init__.py文件中自定义__version__

    keywords = ("erazhan_utils"),
    description = "some common tools in work",
    long_description = "some useful common tools",
    license = "MIT Licence",

    url = "https://github.com/erazhan/erazhan_utils",
    author = "erazhan",
    author_email = "erazhan@163.com",

    python_requires='>=3.6.1',  # 不需要太高的版本
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []  # ["tensorflow==2.2.0","pandas"]#自行安装
)

