# 任务目标： 我们要写一个 “自动化测试框架的核心引擎” 的微缩版。你需要在一个脚本里，把上面学到的所有知识点全部串联起来。
#
# 场景描述： 我们要开发一个 “统一测试数据加载器”。
#
# 系统有一个全局配置（单例），记录了默认要读取的文件路径。
#
# 系统支持多种格式的数据文件（Excel, JSON），需要动态创建加载器（工厂 + 继承 + 多态）。
#
# 加载数据时，需要自动打印耗时（装饰器）。
#
# 必须强制约束所有加载器都有 load() 方法（抽象基类）。
import functools
import time
from abc import ABC, abstractmethod


class FileConfig:
    _instance = None
    _initialize = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filepath):
        if not self._initialize:
            self.filepath = filepath
            self._initialize = True
            print("文件路径配置加载成功······")
        else:
            return


def time_record(func):
    @functools.wraps(func)
    def wrappers(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"方法：{func.__name__}耗时：{end_time-start_time}")
        return result

    return wrappers


class UnionTestDataLoader(ABC):
    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    def load(self):
        pass


class JsonDataLoader(UnionTestDataLoader):
    @time_record
    def load(self):
        print("load Json files······")


class ExcelDataLoader(UnionTestDataLoader):
    @time_record
    def load(self):
        print("load Excel files ·····")


class FactoryDataloader:
    @staticmethod
    def get_loader(filepath):
        if filepath.split(".")[-1] == "json":
            loader = JsonDataLoader(filepath)
        elif filepath.split(".")[-1] == "xlsx":
            loader = ExcelDataLoader(filepath)
        return loader


if __name__ == "__main__":
    filepath = "data.xlsx"
    config = FileConfig(filepath)
    loader = FactoryDataloader.get_loader(config.filepath)
    loader.load()
