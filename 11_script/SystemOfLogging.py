# 作业要求
# 1. 基础日志配置
# 配置一个日志系统，同时输出到控制台和文件
#
# 控制台只显示 WARNING 及以上级别的日志
#
# 文件记录所有 DEBUG 及以上级别的日志
#
# 使用不同的格式：
#
# 控制台：简洁格式，包含时间、级别、消息
#
# 文件：详细格式，包含时间、级别、模块名、函数名、行号、消息

import logging

#创建Logger，设置等级为DEBUG
app_logger = logging.getLogger('app')
app_logger.setLevel(logging.DEBUG)

#设立格式
stream_formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s')

#创建控制台Handler
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
console.setFormatter(stream_formatter)

#创建文件Handler
fileHandler = logging.FileHandler("app.log")
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(file_formatter)

app_logger.addHandler(console)
app_logger.addHandler(fileHandler)
app_logger.propagate = False


# 测试不同级别的日志
app_logger.debug("这是一条调试信息")
app_logger.info("这是一条普通信息")
app_logger.warning("这是一条警告信息")
app_logger.error("这是一条错误信息")

