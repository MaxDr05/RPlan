import pytest
import logging

# 1. 基础功能
# 测试用户注册接口，验证以下场景：
#
# 有效的注册信息
#
# 各种无效的注册信息
#
# 边界情况测试


# 3. 任务目标
# 编写一个参数化测试，能够：
#
# 使用单个测试函数覆盖所有上述场景
#
# 对每个测试用例进行适当的断言验证
#
# 提供清晰的测试报告（使用有意义的测试ID）
#
# 处理成功和失败情况的不同验证逻辑

def set_logger():
    #创建一个logger
    api_logger = logging.getLogger('api_logger')
    api_logger.setLevel(logging.DEBUG)

    # 创建一个formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(lineno)s - %(funcName)s - %(levelname)s - %(message)s')

    #创建2个handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)

    file_handler = logging.FileHandler('test_register.log')
    file_handler.setLevel(logging.DEBUG)

    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    api_logger.addHandler(stream_handler)
    api_logger.addHandler(file_handler)

    return api_logger

logger = set_logger()


test_datas = [
    {
        'username': 'john_doe',
        'password': 'SecurePass123!',
        'email': 'john@example.com',
        'except_result' : '注册成功 (201)'
    },
    {
        'username': 'alice_smith',
        'password': 'AnotherPass456!',
        'email': 'alice.smith@test.com',
        'except_result' : '注册成功 (201)'
    },
    {
        'username': 'jo',
        'password': 'Password123!',
        'email': 'jo@example.com',
        'except_result' : '注册失败 (400)'
    },
    {
        'username': "a"*51,
        'password': 'Password123!',
        'email': 'long@example.com',
        'except_result' : '注册失败 (400)'
    },
    {
        'username': 'bob',
        'password': 'short',
        'email': 'bob@example.com',
        'except_result' : '注册失败 (400)'
    },
    {
        'username': 'charlie',
        'password': 'NoNumbers!',
        'email': 'charlie@example.com',
        'except_result' : '注册失败 (400)'
    },
    {
        'username': 'david',
        'password': 'NoSpecial123',
        'email': 'david@example.com',
        'except_result' : '注册失败 (400)'
    },
    {
        'username': 'eva',
        'password': 'ValidPass123!',
        'email': 'invalid-email',
        'except_result' : '注册失败 (400)'
    },
    {
        'username': 'frank',
        'password': 'ValidPass123!',
        'email': '',
        'except_result' : '注册失败 (400)'
    },
    {
        'username': '',
        'password': 'ValidPass123!',
        'email': 'frank@example.com',
        'except_result' : '注册失败 (400)'
    }
]

@pytest.mark.parametrize('test_datas', test_datas)
def test_register(test_datas):
    logger.debug(f'开始测试---------test_register: {test_datas}')
    result = mock_register_user(test_datas['username'],test_datas['password'], test_datas['email'])
    if test_datas['except_result'] == '注册失败 (400)':
        assert result['status'] == 400
        logger.debug(f'✅测试通过')
    else:
        assert result['status'] == 201
        logger.debug(f'测试通过')

def mock_register_user(username, password, email):
    """
    模拟用户注册函数
    在实际项目中，这里会是真实的API调用
    """
    # 验证用户名
    if not username or len(username) < 3 or len(username) > 50:
        return {"status": 400, "error": "用户名无效"}

    # 验证密码
    if len(password) < 8:
        return {"status": 400, "error": "密码过短"}
    if not any(char.isdigit() for char in password):
        return {"status": 400, "error": "密码必须包含数字"}
    if not any(char in "!@#$%^&*" for char in password):
        return {"status": 400, "error": "密码必须包含特殊字符"}

    # 验证邮箱
    if not email or "@" not in email or "." not in email:
        return {"status": 400, "error": "邮箱格式无效"}

    # 模拟成功注册
    return {
        "status": 201,
        "user_id": f"user_{hash(username)}",
        "username": username,
        "message": "注册成功"
    }