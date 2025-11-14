import pytest
import requests
import json
from requests.exceptions import HTTPError, ConnectionError, Timeout
import logging
import sys

def setup_logger():
    api_logger = logging.getLogger('api_logger')
    api_logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s')

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('test_login.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    api_logger.addHandler(console_handler)
    api_logger.addHandler(file_handler)

    return api_logger

logger = setup_logger()


#数据 - 代码 分离
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
    logger.info(' API接口开始运行测试 ')

    try:
        request = requests.session()
        if method.lower() == 'post':
            logger.debug(f'post开始测试')
            if headers is None:
                headers = {
                    'content-type': 'application/json',
                }

            # 添加调试信息
            logger.debug(f"请求URL: {url}")
            logger.debug(f"请求数据: {data}")
            logger.debug(f"请求头: {headers}")

            # 使用json参数发送数据
            response = request.post(url=url, json=data, timeout=5, allow_redirects=True, headers=headers)
            response.raise_for_status()

        elif method.lower() == 'get':
            logger.debug(f'get开始测试')
            response = request.get(url=url, timeout=5)
            response.raise_for_status()

        # 检查响应状态码
        if response.status_code == 200 or response.status_code == 201:
            logger.debug(f'响应成功 - 状态码: {response.status_code}')

            # 创建结构化的返回结果
            result = {
                "success": True,
                "session": request,
                "response": response,
                "message": f"登录成功 - 状态码: {response.status_code}"
            }
            return result
        else:
            logger.error(f'响应状态码: {response.status_code}')
            result = {
                "success": False,
                "session": request,
                "response": response,
                "message": f"登录失败 - 状态码: {response.status_code}"
            }
            return result

    except HTTPError as e:
        error_msg = f"HTTP错误: {e}"
        logger.error(error_msg)
        result = {
            "success": False,
            "session": None,
            "response": None,
            "message": error_msg
        }
        return result
    except ConnectionError as e:
        error_msg = f"连接错误: {e}"
        logger.error(error_msg)
        result = {
            "success": False,
            "session": None,
            "response": None,
            "message": error_msg
        }
        return result
    except Timeout as e:
        error_msg = f"连接超时: {e}"
        logger.error(error_msg)
        result = {
            "success": False,
            "session": None,
            "response": None,
            "message": error_msg
        }
        return result
    except Exception as e:
        error_msg = f"未知错误导致终止: {e}"
        logger.error(error_msg)
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
        logger.info("✅ 断言通过: 请求成功")
        assert result['response'].status_code in [200,201]
        logger.info(f"✅ 断言通过: 状态码 {result['response'].status_code} 符合预期")

def test_post_login(test_urls):
    # 测试第一个网站
    logger.debug("测试第一个网站 - POST请求:")
    result1 = login_Test(test_urls['url1'], 'post')
    assert result1['success'] == True
    logger.info("✅ 断言通过: 请求成功")
    print("\n" + "=" * 50 + "\n")

def test_get_login(test_urls):
    logger.debug("测试第一个网站 - GET请求:")
    result2 = login_Test(test_urls['url1'], 'get')
    assert result2['success'] == True
    logger.info("✅ 断言通过: 请求成功")
    print("\n" + "=" * 50 + "\n")