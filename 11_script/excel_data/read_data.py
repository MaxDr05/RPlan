import openpyxl
from typing import List, Dict, Any  # 引入类型提示模块
import json


class TestCaseManager:
    def __init__(self, file_path: str):
        self.test_cases = None
        self.group_cases_dict = None
        self.file_path = file_path

    def read_excel_data(self):
        """
        读取 Excel 文件并将每一行转换为字典。
        """

        # 通过路径读取内容sheet页
        wb = openpyxl.load_workbook(filename=self.file_path)
        ws = wb.active

        # 测试用例格式
        keys = [
            "id",
            "module",
            "title",
            "pre_condition",
            "step",
            "expected",
            "priority",
            "type",
            "status",
        ]

        test_cases = []
        for item in ws.iter_rows(min_row=2, values_only=True):
            test_cases.append(dict(zip(keys, item)))

        self.test_cases = test_cases
        return

    def group_cases_by_module(self):
        """
        读取测试用例列表后按照模块进行分类
        """
        group_cases_dict = {}
        for case in self.test_cases:
            if case["module"] in group_cases_dict:
                group_cases_dict[case["module"]].append(case)
            else:
                group_cases_dict[case["module"]] = [case]

        self.group_cases_dict = group_cases_dict
        return

    def save_to_json(self, file_path: str):
        """
        将字典数据保存为 JSON 文件
        Args:
            data: 要保存的数据
            file_path: 保存路径 (例如 'result.json')
        """
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.group_cases_dict, f, indent=4, ensure_ascii=False)
            print("文件已成功保存")


# 预期调用方式 (驾驶手册)
if __name__ == "__main__":
    # 1. 造房 (实例化)
    manager = TestCaseManager("test_cases.xlsx")

    # 2. 装修 (读取)
    manager.read_excel_data()
    print(f"读取到了 {len(manager.test_cases)} 条用例")  # 验证一下

    # 3. 分房间 (分组)
    manager.group_cases_by_module()

    # 4. 拍照留念 (保存)
    manager.save_to_json("final_result.json")
