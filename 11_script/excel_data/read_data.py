import openpyxl

wb = openpyxl.load_workbook("test_cases.xlsx")
ws = wb.active

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


# 需求：生成一个以模块名为键，模块下用例列表为值的字典


grouped_cases = {}

for item in test_cases:
    key = item["module"]
    if key in grouped_cases:
        grouped_cases[key].append(item)
    else:
        grouped_cases[key] = [item]
