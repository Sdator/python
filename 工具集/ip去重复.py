'''
@Author: your name
@Date: 2020-03-19 17:38:42
@LastEditTime: 2020-03-27 17:17:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\工具集\ip去重复.py
'''
# -*- coding: utf-8 -*-
import sys
import os
import re
# 修改当前工作目录为脚本运行目录
os.chdir(os.path.dirname(__file__))


def fun(s):
    # 从右边找到符号.的位置 进行切片
    num = s.rfind('.', 0, -5)
    return s[:num]+".0.0/16"


def main(files):
    with open(files,  encoding='utf-8') as txt:
        # 读入文件 取所有行 去重复
        listIP = set(txt.readlines())
        # 构建地址段 再去重
        listIP = set(list(map(fun, list(listIP))))
        for v in listIP:
            print(v)


def GetStr(lstr: str, s: str) -> str:
    '''
    截获字符串后段\n
    @lstr:    用于过滤的开头字符串\n
    @s:       要处理的字符串\n
    '''
    return re.match(r'^{}(.*)'.format(lstr), s).group(1)


if __name__ == "__main__":
    s = regex.match("abab123").group(1)
    print(s)

    # name = "SMSMB14567.av"
    # # 封装的函数
    # s = GetStr("SM", name)
    # print(s)


    # print(set([1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 1, 1, 1, 1]))
    # PY文件 = os.path.basename(sys.argv[0])
    # 参数 = sys.argv[1]
    # print(PY文件, 参数)

    # s = re.search("^ab(.*)", "ababbcdefa")
