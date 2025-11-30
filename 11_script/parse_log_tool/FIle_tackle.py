# 请写出那个 read_large_file(filepath) 函数，要求：
#
# 使用 with open。
#
# 遍历文件对象 f。
#
# 筛选出包含 "ERROR" 的行。
#
# 使用 yield 返回该行。

import os


def read_large_file(filepath):
    with open(filepath, "r") as f:
        # 【关键修正】直接遍历文件对象 f
        # f 会自动控制进度，读一行，指针移一行，内存里永远只有一行
        for line in f:
            if "ERROR" in line:
                yield line


def get_error_logs(filepath):
    errors = []
    for line in read_large_file(filepath):
        errors.append(line)


if __name__ == "__main__":
    # 这里的路径是写死的，换台电脑就挂了
    file_path = os.path.dirname(os.path.abspath(__file__))

    log_path = os.path.join(file_path, "data", "server.log")

    print(f"filepath:{file_path}")
    print(f"log_path:{log_path}")
