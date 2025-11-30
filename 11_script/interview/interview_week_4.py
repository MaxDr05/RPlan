from numpy.ma.core import logical_or

import parser
import os
import argparse


def parse_arguments():
    # 相当于创建命令行参数的空的菜单
    arg_parser = argparse.ArgumentParser(description="创建命令行参数解析器")

    dir_path = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(dir_path, "logs", "sample.log")

    arg_parser.add_argument(
        "--file", dest="log_file", default=log_path, help="要解析的文件路径"
    )

    return arg_parser.parse_args()


def main():
    args = parse_arguments()
    log_path = args.log_file
    try:
        p = parser.LogParser(log_path)
        result = p.parse()

    except FileNotFoundError as e:
        print(f"文件查询失败，请检查文件路径.错误详细信息:{e}")
    except PermissionError as e:
        print(f"文件权限错误.错误详细信息:{e}")
    except Exception as e:
        print(f"其他错误：{e}")

    if result is None:
        print("解析日志失败")
        return

    with open("parsed_log", "w+", encoding="utf-8") as f:
        for line in result:
            f.writelines(line)
    print("解析日志成功！")


if __name__ == "__main__":
    main()
