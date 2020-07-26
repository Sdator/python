# -*- coding: utf-8 -*-
'''
by 绝 2019.4.27

'''
import lib.AirCom
import sys
import os

# 添加当前工作目录到搜索路径中 为了能让模块找到入口
sys.path.append(os.getcwd())


# from lib.AirCom import *


class MDX(object):

    __字节流 = None
    __贴图数量 = 0

    def __init__(self, 文件):
        self.__file = 文件
        self.__打开文件()

    def __打开文件(self):
        # 二进制模式读取
        with open(self.__file, 'rb') as f:
            self.__字节流 = f.read()

    def 读取贴图路径(self):
        字节流 = self.__字节流
        出现位置 = 字节流.find(b'TEXS')
        贴图数量 = 字节流[出现位置 + 4 + 1]
        当前位置 = 出现位置+8
        贴图路径组 = [字节流[当前位置+268*x:当前位置+268*x +
                     100].strip(b'\x00').decode('utf-8', 'replace') for x in range(贴图数量)]
        贴图路径组.insert(0, os.path.split(self.__file)[1])
        return 贴图路径组

        # decode('utf-8').encode('gb2312')..strip("\x00")


def 目录枚举(path, dest, 后缀):
    files = os.listdir(path)
    for f in files:
        subpath = path + '\\' + f
        # 如果是文件
        if (os.path.isfile(subpath)):
            if os.path.splitext(subpath)[1] == 后缀:
                dest.append(subpath)
        # 如果是目录
        elif (os.path.isdir(subpath)):

            if (f[0] == '.'):
                pass
            else:
                # 递归
                目录枚举(subpath, dest)

        # return self.__file


def 枚举所有模型路径():
    路径 = r'C:\DemoAir\PY'
    路径 = r'D:\OneDrive\War3\模型\资源\微光战记'

    路径组 = []
    目录枚举(路径, 路径组, ".rms")

    贴图路径 = []
    for f in 路径组:
        print(f)
        a = MDX(f)
        贴图路径.append(a.读取贴图路径())

    print(贴图路径)
    写出文件("1.json", 贴图路径)


if __name__ == '__main__':
    枚举所有模型路径()


'''
os.listdir          目录枚举
os.path.isdir       是否目录
os.path.splitext    %~x0   分割文件名和后缀
os.path.split       %~nx0  分割路径和文件名


'''
