

def ls(path, **info, ):
    print(path, info["name"])


def lss(*info, path=".", **infos):
    print(path, info, infos)


ls(123, name="true")                # 正规写法 一个未知多变参数
ls(111, paths=454, name="true")     # 正规写法 可以带多个未知的参数
ls(name="true", path=454)           # 键值写法
ls(name="true")                     # 带默认参数写法 可以去掉第一个参数


# lss(name=True, path=".")
# lss(path=".", name=True)
# lss(".", name=True)
# Split-Path
# Get-Content
