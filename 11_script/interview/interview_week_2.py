# 实战场景： 我们需要一个日志解析工具，处理两种日志：
# 通用文本日志：直接读取每一行。
# JSON 格式日志：每一行是一个 JSON 字符串，需要解析出里面的 'timestamp' 字段。
# 你的任务： 编写代码，包含以下要素：
# 定义基类 BaseLogParser，包含抽象方法 parse(self)（提示：用 NotImplementedError 模拟抽象类）。
# 定义子类 JsonLogParser 继承基类，重写 parse 方法。
# 核心要求：写一个装饰器 @log_execution，打印出 parse 方法开始执行和结束执行的时间。并把它应用在子类的 parse 方法上。
# 必须使用 super() 和 functools.wraps。
# Show me the code. （请在编辑器里写完再发给我，不要有语法错误）”

from functools import wraps
import time, json


def log_execution(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"运行时间为{end_time-start_time}")
        return result

    return wrappers


class BaseLogParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def parse(self):
        raise NotImplementedError


class JsonLogParser(BaseLogParser):
    def __init__(self, filepath):
        super().__init__(filepath)

    @log_execution
    def parse(self):
        time_stamp_lists = []
        with open(file=self.filepath, mode="r", encoding="utf-8") as f:
            for line in f:
                json_line = json.loads(line)
                if "timestamp" in json_line:
                    time_stamp_lists.append(json_line["timestamp"])
        return time_stamp_lists
