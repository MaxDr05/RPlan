import pytest

api_cases = [
    {"url": "/home", "method": "GET", "expected": 200},
    {"url": "/login", "method": "POST", "expected": 201},
    {"url": "/admin", "method": "GET", "expected": 403},
]


@pytest.mark.parametrize("case_info", api_cases)
def test_api_status(case_info):
    method = case_info["method"]
    url = case_info["url"]
    print(f"\n正在请求: {method} {url}")
    assert case_info["expected"] > 0
