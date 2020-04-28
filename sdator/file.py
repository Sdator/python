# -*- coding: utf-8 -*-

from datetime import datetime
import json
import path as pb


def 写出文件(关键字, data, 读写方式="a", 写出格式="json"):
    """
    `参数1` 写出路径

    `参数2` 写出的数据

    `参数3` 读写方式 默认为追加模式

    `参数4` 写出格式 默认为json格式自动转码
    """
    # 构建命名规则
    日期 = datetime.now().strftime("%Y%m%d")
    路径 = pb.File("/json/%s_%s.%s" % (日期, 关键字, 写出格式))
    路径.创建目录Ex()

    # 如果不是字符串就转码
    if not isinstance(data, str):
        data = json.dumps(data, ensure_ascii=False)+"\n"

    # 打开文件
    with open(路径.绝对路径, 读写方式, encoding="utf-8") as f:
        # 写到文件
        f.write(data)
    # 返回写出路径
    return 路径.绝对路径
