import pytest
import requests
import json
from requests.exceptions import HTTPError, ConnectionError, Timeout

@pytest.fixture(scope="module")
def test_urls():
    return {
        'url1': 'https://jsonplaceholder.typicode.com/posts',
        'url2': 'https://reqres.in/api/login',
    }

@pytest.fixture(scope="module")
def test_data():
    return {
        'jsonplaceholder': {
            'title': 'Test Post',
            'body': 'This is a test post from our login script',
            'userId': 1
        },
        'reqres': {
            'email': 'eve.holt@reqres.in',
            'password': 'cityslicka'
        }
    }

#输入：目标网址，请求方法
#输出：结果字典，包含结果状态，连接，响应，信息

def login_Test(url, method,data = None,headers = None):
    print('登陆脚本运行', '-' * 8)


    try:
        request = requests.session()
        if method.lower() == 'post':
            if headers is None:
                headers = {
                    'content-type': 'application/json',
                }

            # 添加调试信息
            print(f"请求URL: {url}")
            print(f"请求数据: {data}")
            print(f"请求头: {headers}")

            # 使用json参数发送数据
            response = request.post(url=url, json=data, timeout=5, allow_redirects=True, headers=headers)
            response.raise_for_status()

        elif method.lower() == 'get':
            response = request.get(url=url, timeout=5)
            response.raise_for_status()

        # 检查响应状态码
        if response.status_code == 200 or response.status_code == 201:
            print(f'响应成功 - 状态码: {response.status_code}')
            print("响应内容:")
            print(response.json())

            # 创建结构化的返回结果
            result = {
                "success": True,
                "session": request,
                "response": response,
                "message": f"登录成功 - 状态码: {response.status_code}"
            }
            return result
        else:
            print(f'响应状态码: {response.status_code}')
            result = {
                "success": False,
                "session": request,
                "response": response,
                "message": f"登录失败 - 状态码: {response.status_code}"
            }
            return result

    except HTTPError as e:
        error_msg = f"HTTP错误: {e}"
        print(error_msg)
        result = {
            "success": False,
            "session": None,
            "response": None,
            "message": error_msg
        }
        return result
    except ConnectionError as e:
        error_msg = f"连接错误: {e}"
        print(error_msg)
        result = {
            "success": False,
            "session": None,
            "response": None,
            "message": error_msg
        }
        return result
    except Timeout as e:
        error_msg = f"连接超时: {e}"
        print(error_msg)
        result = {
            "success": False,
            "session": None,
            "response": None,
            "message": error_msg
        }
        return result
    except Exception as e:
        error_msg = f"未知错误导致终止: {e}"
        print(error_msg)
        result = {
            "success": False,
            "session": None,
            "response": None,
            "message": error_msg
        }
        return result

class TestLogin:
    def test_post_jsonplaceholder(self, test_urls, test_data):
        result = login_Test(test_urls['url1'], 'post',data = test_data['jsonplaceholder'])
        assert result['success'] == True
        assert result['response'].status_code in [200,201]

def test_post_login(test_urls):
    # 测试第一个网站
    print("测试第一个网站 - POST请求:")
    result1 = login_Test(test_urls['url1'], 'post')
    assert result1['success'] == True
    print("\n" + "=" * 50 + "\n")

def test_get_login(test_urls):
    print("测试第一个网站 - GET请求:")
    result2 = login_Test(test_urls['url1'], 'get')
    assert result2['success'] == True
    print("\n" + "=" * 50 + "\n")