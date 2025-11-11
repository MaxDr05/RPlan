import pytest,requests,time
from requests.exceptions import HTTPError,ConnectionError,Timeout

# 基础任务
# 选择一个公开的 API 端点进行测试（推荐使用免费的公共 API）
# 使用 requests 库发送 GET 请求
# 断言响应状态码为 200
# 编写相应的测试函数

# 扩展任务（可选）
# 如果你完成基础任务后想进一步练习：
#
# 添加多个断言：
# 断言响应内容类型是 application/json
# 断言响应时间小于 3 秒
# 断言响应头包含特定的字段
#
# 测试异常情况：
# 测试一个返回 404 的端点
# 使用 pytest.raises 处理请求异常
#
# 使用夹具：
# 创建夹具来设置请求会话
# 创建夹具来提供测试数据

url = 'https://jsonplaceholder.typicode.com/posts/1'
url_404 = 'https://httpbin.org/status/404'

@pytest.fixture
def api_session():
    """共享的请求会话，避免重复创建"""
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    return session

@pytest.fixture
def test_urls():
    return {
        'SUCCESS': url,
        'NOT_FOUND': url_404,
        'server_error': 'https://httpbin.org/status/500',
        'connection_error': 'https://invalid-domain-12345.com',
    }

@pytest.fixture(scope='module')
def common_response_data(api_session, test_urls):
    """共享的响应数据，避免重复请求"""
    print("common_response_data开始运行！")
    response = api_session.get(test_urls['SUCCESS'])
    result = {
        'response': response,
        'json_data': response.json(),
        'headers': response.headers,
        'status_code': response.status_code
    }
    print('common_response_data结束运行')
    return result


def get_response(api_session,test_urls):
    try:
        response = api_session.get(test_urls['SUCCESS'])
        response.raise_for_status()
        return response

    except HTTPError as http_err:
        raise http_err
    except ConnectionError as conn_err:
        raise conn_err
    except Timeout as timeout_err:
        raise timeout_err
    except Exception as err:
        raise err


def test_get_200(api_session,test_urls):
    response = api_session.get(test_urls['SUCCESS'])
    assert response.status_code == 200
def test_returnType(common_response_data):
    print(">>> 运行 test_returnType")
    assert 'application/json' in common_response_data['headers']['Content-Type']
def test_json_structure(common_response_data):
    """测试2：也使用共享响应数据"""
    print(">>> 运行 test_json_structure")
    data = common_response_data['json_data']
    assert 'id' in data

def test_runtime(api_session,test_urls):
    start_time = time.time()
    response = api_session.get(test_urls['SUCCESS'])
    end_time = time.time()
    assert end_time - start_time < 3
def test_existMaxAge(api_session,test_urls):
    response = api_session.get(test_urls['SUCCESS'])
    assert 'max_age' in response.headers['nel']

def test_404(api_session,test_urls):
    with pytest.raises(requests.exceptions.HTTPError):
        response = api_session.get(test_urls['NOT_FOUND'])
        response.raise_for_status()

def test_connection_error(api_session,test_urls):
    """测试网络连接错误"""
    with pytest.raises(ConnectionError):
        api_session.get(test_urls['connection_error'],timeout=5)

def test_timeout_error(api_session,test_urls):
    """测试请求超时"""
    with pytest.raises(Timeout):
        api_session.get(test_urls['SUCCESS'],timeout=0.01)