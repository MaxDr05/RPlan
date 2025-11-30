# 🛠️ 实战任务：重构日志解析工具
# 我们要搭建一个通用的日志解析系统。
#
# 第一步：设计父类 (BaseLogParser)
#
# 我们需要一个“基类”，它定义了所有解析器都必须遵守的规则。
#
# 请尝试写一个名为 BaseLogParser 的类。 要求：
#
# 包含 __init__ 方法，接收 file_path 并存为属性。
#
# 定义一个 parse 方法。
#
# 思考：作为基类，它不知道具体怎么解析（因为不知道是 CSV 还是 Excel），所以这个方法里应该写什么？（是直接写逻辑，还是留空，或者抛出一个错误提示子类必须实现？）
#
# 请试着把这个 BaseLogParser 的代码写出来看看？
import time
from abc import ABC, abstractmethod


# 装饰器-计时
def timer(func):

    def wrappers(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"方法耗时：{end_time - start_time}")
        return result

    return wrappers


class BaseLogParser(ABC):
    def __init__(self, filepath):
        self.filepath = filepath

    def read_file(self):
        with open(file=self.filepath, mode="r", encoding="utf-8") as f:
            return f.readlines()

    # def parse(self):
    #     raise NotImplementedError
    @abstractmethod
    def parser(self):
        pass


class SerialLogParser(BaseLogParser):
    @timer
    def parser(self):
        data_lines = self.read_file()
        for line in data_lines:
            if "ERROR" in line:
                print(line)


class JsonLogParser(BaseLogParser):
    def __str__(self):
        return f"JsonLogParser:{self.filepath}"

    @timer
    def parser(self):
        data_lines = self.read_file()
        for line in data_lines:
            if "ERROR" in line:
                print(line)


class ParseFactory:
    @staticmethod
    def get_parser(file_path):
        file_type = file_path.split(".")[-1]

        if file_type == "json":
            parser = JsonLogParser(file_path)
        elif file_type == "log":
            parser = SerialLogParser(file_path)
        else:
            raise ValueError(f"读取到无法识别的文件类型：{file_type}")
        return parser


if __name__ == "__main__":
    parser1 = ParseFactory.get_parser("applog.json")
    print(parser1)
    try:
        parser2 = ParseFactory.get_parser("applog.png")
    except ValueError as e:
        print(f"捕获到valueError:{e}")
