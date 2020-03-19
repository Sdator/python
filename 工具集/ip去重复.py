# -*- coding: utf-8 -*-
import sys
import os

# 修改当前工作目录为脚本运行目录
os.chdir(os.path.dirname(__file__))

def fun(s):
    # 从右边找到符号.的位置 进行切片
    num = s.rfind('.', 0, -5)
    return s[:num]+".0.0/16"


def main(files):
    # print(sys.argv[0])
    # print(os.getcwd())
    # print(__file__)
    # print(os.path.realpath(__file__))
    # print(os.path.split(os.path.realpath(__file__))[0])
    # print(os.path.dirname(os.getcwd()))
    with open(files,  encoding='utf-8') as txt:
        # 读入文件 取所有行 去重复
        listIP = set(txt.readlines())
        # 构建地址段 再去重
        listIP = set(list(map(fun, list(listIP))))
        for v in listIP:
            print(v)


if __name__ == "__main__":
    main("ip.txt")
