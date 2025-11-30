# def add_case(case_name, case_list=None):
#     if case_list == None:
#         case_list = []
#     case_list.append(case_name)
#     return case_list
#
#
# print(add_case("Case A"))
# print(add_case("Case B"))

# 你的任务： 编写一个函数 read_excel(file_path)。 要求：
#
# 使用 openpyxl 读取数据。
# 核心难点：返回值必须是 List 嵌套 Dict 的格式。
# 也就是：[{'case_id': 1, 'title': '正常登录'...}, {'case_id': 2...}]
# 不能写死 Key，代码必须自动把第一行的表头作为 Key，把下面的每一行数据作为 Value 拼装起来。
# 要体现代码规范（变量命名清晰，有注释）。

import openpyxl
from typing import List, Dict, Any


def read_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    读取excel文件，读取数据,将每个用例生成为dict后打包为list

    Args:
        file_path:excel文件路径

    Returns:
        test_cases:用例字典列表
    """
    wb = openpyxl.load_workbook(filename=file_path, data_only=True)
    ws = wb.active

    test_cases = []

    # 表头获取键值
    rows = ws.iter_rows(values_only=True)
    keys = next(rows)

    for row in rows:
        if not all(row):
            continue
        test_cases.append(dict(zip(keys, row)))
    return test_cases
