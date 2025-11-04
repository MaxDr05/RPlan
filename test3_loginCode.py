import requests
import json
from requests.exceptions import HTTPError, ConnectionError, Timeout

urls = {
    'url1': 'https://jsonplaceholder.typicode.com/posts',
    'url2': 'https://reqres.in/api/login',
}


def login_Test(url, username, password, method):
    print('登陆脚本运行', '-' * 8)

    # 为jsonplaceholder准备测试数据
    data = {
        'title': 'Test Post',
        'body': 'This is a test post from our login script',
        'userId': 1
    }

    try:
        request = requests.session()
        if method.lower() == 'post':
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


# 测试第一个网站
print("测试第一个网站 - POST请求:")
result1 = login_Test(urls['url1'], 'testuser', 'testpass', 'post')
print("\n" + "=" * 50 + "\n")

print("测试第一个网站 - GET请求:")
result2 = login_Test(urls['url1'], 'testuser', 'testpass', 'get')