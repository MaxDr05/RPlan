# 作业目标
# 选择一个免费的公共API，发送请求并分析返回的数据结构。
#
# 作业要求
# 基础任务：
# 选择API：从以下推荐中选择一个免费的公共API
#
# 发送请求：使用Python的requests库发送GET请求
#
# 处理响应：检查HTTP状态码，处理可能的异常
#
# 分析数据：解析返回的JSON数据并提取关键信息
#
# 推荐API列表：
# JSONPlaceholder：https://jsonplaceholder.typicode.com/posts
# 需要展示的信息：
# API返回的数据结构
#
# 关键字段的值
#
# 数据总量统计
#
# 遇到的任何错误及处理方式
import requests
from requests.exceptions import ConnectionError,HTTPError,Timeout

url = 'https://jsonplaceholder.typicode.com/posts'
try :
    response = requests.get(url=url)
    response.raise_for_status()

    print(f'返回相应码{response.status_code}')
    print('-'*20)
    # print(f'返回的数据结构{response.headers.get('content-type','')}')
    # print('-' * 20)
    # print('响应头字段值：')
    # for k,v in response.headers.items():
    #     print(f'{k}: {v}')
    # print('-' * 20)
    # print(f'数据总量：{len(response.json())}')
    print('-' * 20)
    print(f'json内容：{response.json()}')

    content_response = response.json()
    print('-' * 20)
    print(f'帖子数量:{len(content_response)}')
    print('-' * 20)
    print(f'第一个帖子的详细内容:')
    for k,v in content_response[0].items():
        print(f'{k}: {v}')
    print('*'*20)
    print(f'获取所有帖子的标题:')
    for k in content_response:
        print(f'标题：{k.get('title',' ')}')

except HTTPError as e:
    print(f'HTTPError: {e}')
except ConnectionError as e:
    print(f'ConnectionError: {e}')
except Timeout as e:
    print(f'Timeout: {e}')
except Exception as e:
    print(f'Exception: {e}')


