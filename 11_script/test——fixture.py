import pytest

@pytest.fixture(scope="function")
def function_scope():
    """默认作用域，每个测试函数执行一次"""
    print("函数级别夹具 - 设置")
    yield
    print("函数级别夹具 - 清理")

@pytest.fixture(scope="class")
def class_scope():
    """类级别，每个测试类执行一次"""
    print("类级别夹具 - 设置")
    yield
    print("类级别夹具 - 清理")

@pytest.fixture(scope="module")
def module_scope():
    """模块级别，每个测试模块执行一次"""
    print("模块级别夹具 - 设置")
    yield
    print("模块级别夹具 - 清理")

@pytest.fixture(scope="session")
def session_scope():
    """会话级别，整个测试会话执行一次"""
    print("会话级别夹具 - 设置")
    yield
    print("会话级别夹具 - 清理")


class TestScopeExample:
    def test_one(self, function_scope, class_scope, module_scope, session_scope):
        assert True

    def test_two(self, function_scope, class_scope, module_scope, session_scope):
        assert True


def test_another(function_scope, module_scope, session_scope):
    assert True