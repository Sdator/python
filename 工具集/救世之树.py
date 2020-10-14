'''
# 2020.10.14
作者：絕版大叔、    QQ 250740270
用途:
    修改语音为日语
    汉化游戏
'''

# %%

import subprocess  # 执行终端命令
import os
from lxml import etree  # xml处理
import time


# 修改当前工作目录为脚本运行目录
os.chdir(os.path.dirname(__file__))


def now(): return time.time()


class GetAttrError(ValueError):
    pass


def main():
    # 找到 xml 路径  利用 everything 的 ctl 工具快速搜索
    sh = r'es -r \\steamapps\\common\\TreeOfSavior\\release\\user.xml$'
    (_, output) = subprocess.getstatusoutput(sh)
    xmlfile = output.split("\n")[0]  # 分割路径 取第一个

    # 找到节点
    root = etree.parse(xmlfile).getroot()
    sound = root.xpath("//Sound[@Language]")[0]

    # 更新属性
    attr = "Language"
    if not(attr in sound.attrib):
        raise GetAttrError('找不到 Language 属性')  # 找不到属性 抛出错误 自定义的
    sound.attrib[attr] = "Japanese"

    # 解析 xml 为二进制数据
    data = etree.tostring(root, pretty_print=True,
                          xml_declaration=True, encoding='UTF-8')

    # 写回文件中
    f = open(xmlfile, "wb")
    f.write(data)
    f.close()


if __name__ == "__main__":
    t = now()
    print("开始")
    try:
        main()
    except OSError as e:
        print("找不到文件", e)
    except IndexError as e:
        print("无法匹配到节点：", e)
    except GetAttrError as e:
        print("属性不存在", e)

    print("结束, 本次操作耗时 %.2f 秒" % (now()-t))
