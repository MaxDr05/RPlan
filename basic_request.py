import requests
from requests.exceptions import HTTPError, ConnectTimeout
url_get = 'https://httpbin.org/get'
url_post = 'https://httpbin.org/post'

try:
    params = {
        'username': 'admin',
        'password': '123',
    }
    response = requests.get(url_get,params=params)
    response.raise_for_status()
    print(f'返回状态码：{response.status_code}')
    # print(response.status_code)
    print('-'*10)
    print(f'打印响应头：{response.headers}')
    print('-' * 10)
    print('尝试打印相应内容的json格式：')
    print(response.text)

    print('-' * 10)
    print('尝试使用post请求')
    print('-' * 10)
    data = {
        'username': 'admin',
        'password': '2222',
    }
    response = requests.post(url_post,data=data)
    response.raise_for_status()
    print('-' * 10)
    print(f'打印响应头：{response.headers}')
    print('-' * 10)
    print(f'尝试打印相应内容的json格式：{response.json()}')
    print('-' * 10)
    print(f'打印请求头{response.request.headers}')
except HTTPError as err:
    print(f'出现HTTPError: {err}')

except ConnectTimeout as err:
    print(f'出现🔗错误！ ConnectTimeout: {err}')

except Exception as err:
    print(f'未知错误！error: {err}')