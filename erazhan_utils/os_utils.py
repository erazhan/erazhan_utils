# -*- coding = utf-8 -*-
# @time: 2022/2/21 10:52 上午
# @Author: erazhan
# @File: os_utils.py

# ----------------------------------------------------------------------------------------------------------------------

import os

def test_os__path__dirname():
    # 得到当前文件的绝对路径
    print(os.path.dirname(os.path.abspath(__file__)))


def test_os__listdir(dir_path):
    # 得到指定文件夹下所有的文件和文件夹
    for one in os.listdir(dir_path):
        print(dir_path + one)


def test_os__path__isfile_or_isdir(file_or_dir_path):
    # 判断路径是文件还是文件夹
    if os.path.isfile(file_or_dir_path):
        print(file_or_dir_path, "is a file:")
    if os.path.isdir(file_or_dir_path):
        print(file_or_dir_path, "is a dir")


def test_os__path__exist(file_or_dir_path="./ostools.py"):
    ans = os.path.exists(file_or_dir_path)
    print("file_or_dir_path", file_or_dir_path, "\nans:", ans)


def test_os__getcwd():
    # 获取当前路径
    ans = os.getcwd()
    print(ans)


if __name__ == "__main__":
    test_os__path__exist()
    pass