import pytest
from api_client import ReqresClient


class TestReqres:

    def test_get_users_success(self, api_client):
        """测试查询用户列表 (切换到 httpbin 源)"""
        # 调用接口
        res = api_client.list_users(page=2)

        # 防御性断言
        assert res is not None, "接口请求失败，返回了 None"

        print("\n正在检查数据...")

        # httpbin 会把你传的 params 放在 'args' 字段里返回
        # 这里的 page 应该是字符串 '2'，因为 URL 参数传输时都是字符串
        assert res["args"]["page"] == "2"

        # 验证你的 User-Agent 是否真的带上了
        assert "Mozilla" in res["headers"]["User-Agent"]

    def test_create_user_consistency(self, api_client):
        """测试创建用户后，返回的数据与输入一致"""
        name = "neo"
        job = "leader"

        res = api_client.create_user(name=name, job=job)

        # httpbin 会把 body 数据放在 'json' 里
        assert res["json"]["name"] == name
        assert res["json"]["job"] == job

    # 🟢 只需要请求 new_user 这个 fixture
    def test_workflow_lifecycle(self, new_user):
        """测试用户生命周期闭环"""

        # 当代码运行到这里时，Setup 已经跑完了，new_user 就是 yield 出来的数据
        print(f"正在测试用户: {new_user['name']}")

        # 验证 Fixture 真的帮我创建了用户
        assert new_user["name"] == "test_user_007"

        # ... 测试结束 ...
        # (此时，Pytest 会自动跳回 conftest.py 执行 delete_user)
