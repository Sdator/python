
import os


class File:

    def __init__(self, path):
        self.__path = path

    @property
    def 取文件名(self):
        return os.path.basename(self.__path)

    @property
    def 是否绝对路径(self):
        return os.path.isabs(self.__path)

    @property
    def 文件是否存在(self):
        return os.path.isfile(self.取路径)

    @property
    def 路径是否存在(self):
        return os.path.exists(self.__path)

    @property
    def 取合格路径(self):
        return os.path.realpath(self.__path)

    @property
    def 目录是否存在(self):

        return os.path.isdir(self.取路径)

    @property
    def 构造绝对路径(self):
        return os.path.abspath(self.__path)

    @property
    def 绝对路径(self):

        path = File(self.获取工作目录 + self.__path)
        return path.构造绝对路径

    @property
    def 获取工作目录(self):
        return os.getcwd()

    @property
    def 取路径(self):
        return os.path.dirname(self.__path)

    def 创建目录Ex(self):
        绝对目录 = File(self.绝对路径)

        if 绝对目录.目录是否存在:
            return
        # 创建目录
        os.makedirs(绝对目录.取路径)
