# 任务1：基础POST请求
# 创建一个函数，向 https://httpbin.org/post 发送POST请求，要求：
# 使用表单数据格式发送用户注册信息
# 包含用户名、邮箱、密码三个字段
# 处理可能出现的网络异常
# 记录请求和响应的详细信息
import requests
import json
from requests.exceptions import HTTPError,ConnectionError,Timeout
def task_1():
    try:
        print('任务一：发送post请求')
        data = {
            'username': 'admin',
            'password': '111111',
            'email': '111@gmail.com',
        }

        response = requests.post(
            url='http://httpbin.org/post',data=data )

        response.raise_for_status()

        print('-'*8)
        result = response.json()
        print(result['form']['username'])

    except HTTPError as e:
        print(f"HTTPError: {e}")
    except ConnectionError as e:
        print(f"ConnectionError: {e}")
    except Timeout as e:
        print(f"Timeout: {e}")
    except Exception as e:
        print(f"Exception: {e}")

# task_1()

# 任务2：JSON数据提交
# 创建一个商品添加功能，要求：
# 向 https://httpbin.org/post 发送JSON格式的商品信息
# 商品信息包括：名称、价格、分类、库存数量
# 使用正确的Content-Type头
# 验证服务器是否正确解析了JSON数据
def task_2():
    try:
        print('任务二：JSON数据提交')
        parmas = {
            'name': 'apple',
            'price': '4',
            'catagory': 'fruit',
            'stock':'100'
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            url='http://httpbin.org/post',data = json.dumps(parmas),headers=headers )

        response.raise_for_status()

        print('-'*8)
        result = response.json()
        print(result['json']['name'])

    except HTTPError as e:
        print(f"HTTPError: {e}")
    except ConnectionError as e:
        print(f"ConnectionError: {e}")
    except Timeout as e:
        print(f"Timeout: {e}")
    except Exception as e:
        print(f"Exception: {e}")

task_2()