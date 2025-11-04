import requests

# 测试不同的Content-Type
test_cases = [
    {
        'name': '表单数据',
        'headers': {'Content-Type': 'application/x-www-form-urlencoded'},
        'data': {'key': 'value', 'name': 'test'}
    },
    {
        'name': 'JSON数据',
        'headers': {'Content-Type': 'application/json'},
        'data': '{"key": "value", "name": "test"}'  # 字符串形式的JSON
    },
    {
        'name': '使用json参数（推荐）',
        'headers': {},
        'json': {'key': 'value', 'name': 'test'}  # 使用json参数，requests自动处理
    }
]

for case in test_cases:
    print(f"\n测试: {case['name']}")

    # 准备请求参数
    request_kwargs = {
        'url': 'https://httpbin.org/post',
        'headers': case['headers']
    }

    # 根据测试用例添加数据
    if 'data' in case:
        request_kwargs['data'] = case['data']
    if 'json' in case:
        request_kwargs['json'] = case['json']

    response = requests.post(**request_kwargs)
    result = response.json()

    print(f"请求头Content-Type: {result['headers'].get('Content-Type')}")

    # 正确显示所有相关数据字段
    print("=== 响应数据分解 ===")
    if result.get('form'):
        print(f"表单数据 (form): {result['form']}")
    if result.get('data'):
        print(f"原始数据 (data): {result['data']}")
    if result.get('json'):
        print(f"JSON数据 (json): {result['json']}")
    if result.get('files'):
        print(f"文件数据 (files): {result['files']}")