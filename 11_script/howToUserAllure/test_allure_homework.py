#用户管理api测试


import logging
from typing import Optional
from venv import logger

import pytest
import allure

def setup_logger():
    logger = logging.getLogger("UserManager")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(lineno)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("UserManager.log")
    file_handler.setLevel(logging.INFO)

    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()

def user_data():
    return [
        {
            'username' : 'Calvin',
            'email' : '1111@qq.com',
            'password' : '888888888',
            'role' : 'user',
            'description' : '成功创建用户',
            'except_result' : True
        },
        {
            'username' : 'Ca',
            'email' : '1111@qq.com',
            'password' : '888888888',
            'role' : 'user',
            'description' : '用户名过短',
            'except_result' : False
        },
        {
            'username': 'Calvin'*6,
            'email': '1111@qq.com',
            'password': '888888888',
            'role': 'user',
            'description': '用户名过长',
            'except_result': False
        },
        {
            'username': 'Calvin2',
            'email': '1111@qq.com',
            'password': '88',
            'role': 'user',
            'description': '密码过短',
            'except_result': False
        },
        {
            'username': 'Calvin3',
            'email': '1111qq.com',
            'password': '888888888',
            'role': 'user',
            'description': '邮箱格式不正确',
            'except_result': False
        },
        {
            'email': '1111@qq.com',
            'password': '888888888',
            'role': 'user',
            'description': '缺少必填字段',
            'except_result': False
        },
        {
            'username': 'Calvin',
            'email': '1111@qq.com',
            'password': '888888888',
            'role': 'user',
            'description': '用户名重复',
            'except_result': False
        },
    ]




#待测试的api
import json
from typing import Dict, Optional


class UserManagementAPI:
    """用户管理API模拟类"""

    def __init__(self):
        self.users = {}
        self.next_id = 1

    def create_user(self, user_data):
        """
        创建用户

        Args:
            user_data: 用户数据，包含 username, email, password, role 等字段

        Returns:
            创建结果，包含 success, user_id, message 等字段
        """
        # 验证必填字段
        required_fields = ["username", "email", "password"]
        for field in required_fields:
            if field not in user_data or not user_data[field]:
                return {
                    "success": False,
                    "message": f"缺少必填字段: {field}",
                    "status_code": 400
                }

        # 验证用户名长度
        if len(user_data["username"]) < 3:
            return {
                "success": False,
                "message": "用户名至少需要3个字符",
                "status_code": 400
            }

        if len(user_data["username"]) > 20:
            return {
                "success": False,
                "message": "用户名不能超过20个字符",
                "status_code": 400
            }

        # 验证密码强度
        if len(user_data["password"]) < 8:
            return {
                "success": False,
                "message": "密码至少需要8个字符",
                "status_code": 400
            }

        # 验证邮箱格式
        if "@" not in user_data["email"]:
            return {
                "success": False,
                "message": "邮箱格式不正确",
                "status_code": 400
            }

        # 检查用户名是否已存在
        for user in self.users.values():
            if user["username"] == user_data["username"]:
                return {
                    "success": False,
                    "message": "用户名已存在",
                    "status_code": 409
                }

        # 创建用户
        user_id = self.next_id
        self.users[user_id] = {
            "id": user_id,
            "username": user_data["username"],
            "email": user_data["email"],
            "role": user_data.get("role", "user"),
            "status": "active"
        }
        self.next_id += 1

        return {
            "success": True,
            "user_id": user_id,
            "message": "用户创建成功",
            "status_code": 201
        }

    def get_user(self, user_id: int):
        """
        获取用户信息

        Args:
            user_id: 用户ID

        Returns:
            用户信息字典，如果用户不存在返回None
        """
        return self.users.get(user_id)

    def update_user(self, user_id: int, update_data):
        """
        更新用户信息

        Args:
            user_id: 用户ID
            update_data: 要更新的字段

        Returns:
            更新结果
        """
        if user_id not in self.users:
            return {
                "success": False,
                "message": "用户不存在",
                "status_code": 404
            }

        # 更新允许的字段
        allowed_fields = ["email", "role", "status"]
        for field in update_data:
            if field in allowed_fields:
                self.users[user_id][field] = update_data[field]

        return {
            "success": True,
            "message": "用户信息更新成功",
            "status_code": 200
        }

    def delete_user(self, user_id: int):
        """
        删除用户

        Args:
            user_id: 用户ID

        Returns:
            删除结果
        """
        if user_id not in self.users:
            return {
                "success": False,
                "message": "用户不存在",
                "status_code": 404
            }

        del self.users[user_id]
        return {
            "success": True,
            "message": "用户删除成功",
            "status_code": 200
        }

    def list_users(self, role: str = None):
        """
        获取用户列表

        Args:
            role: 按角色过滤（可选）

        Returns:
            用户列表
        """
        users_list = list(self.users.values())

        if role:
            users_list = [user for user in users_list if user.get("role") == role]

        return {
            "success": True,
            "users": users_list,
            "total": len(users_list),
            "status_code": 200
        }



@allure.feature('用户管理功能')
class TestUserManager:
    user_api = UserManagementAPI()


    @pytest.mark.parametrize("test_case", user_data())
    @allure.story('用户注册功能')
    def test_register_user(self, test_case):
        allure.dynamic.title(f'测试用例：{test_case['description']}')
        logger.info(f"测试用例{test_case['description']}")
        with allure.step(f'测试场景{test_case['description']}'):
            test_data = f'''
                        测试用户名：{test_case['username'] if 'username' in test_case.keys() else '无用户名'},'
                        测试密码：{test_case['password']}'
                        测试邮箱：{test_case['email']}
                        '''
            allure.attach(test_data,name='注册数据详情',
                          attachment_type=allure.attachment_type.TEXT)


        with allure.step(f'创建用户'):
            result = self.user_api.create_user(test_case)
            result_json = json.dumps(result,ensure_ascii=False)
            allure.attach(result_json,name='返回内容',
                          attachment_type=allure.attachment_type.JSON)

        with allure.step('验证结果'):
            assert result['success'] == test_case['except_result']