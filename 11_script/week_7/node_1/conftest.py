import pytest
from api_client import ReqresClient


# @pytest.fixture 是装饰器，标记下面这个函数是一个“固件”
# scope="session" 是关键：
# 意味着整个测试过程（不管有多少个用例文件），这个函数只运行 1 次！
# 相当于实现了“单例模式”，极大地节省了创建对象和建立 TCP 连接的开销。
@pytest.fixture(scope="session")
def api_client():
    """
    初始化 API 客户端，供所有测试用例使用
    """
    print("\n[Fixture] 正在初始化 API 客户端 (只执行一次)...")
    # 实例化我们在上一节修改好的 httpbin 客户端
    client = ReqresClient(host="https://httpbin.org")
    return client


@pytest.fixture
def new_user(api_client):
    """
    [Setup] 创建一个临时用户
    [Yield] 把用户数据传给测试用例
    [Teardown] 删除这个用户
    """
    user_name = "test_user_007"
    print(f"\n[Setup] 正在创建临时用户: {user_name}...")

    # 1. 调接口创建
    api_client.create_user(name=user_name, job="tester")

    # 模拟返回的用户数据 (因为 httpbin 不会真存，我们自己构造一个对象给用例用)
    user_data = {"name": user_name, "id": "999"}

    # 2. 交付 (暂停点)
    yield user_data

    # 3. 恢复环境 (Teardown)
    print(f"\n[Teardown] 正在清理垃圾数据: {user_name}...")
    api_client.delete_user(name=user_name)
