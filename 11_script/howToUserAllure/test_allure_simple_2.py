import allure
import pytest


@allure.feature("用户管理")
@allure.story("用户注册")
class TestUserRegistration:
    # 测试数据
    test_cases = [
        ("valid_user", "StrongPass123!", "test@example.com", True, "有效注册"),
        ("short", "Weak123!", "test@example.com", False, "用户名过短"),
        ("valid_user", "123", "test@example.com", False, "密码过短"),
    ]

    @pytest.mark.parametrize("username,password,email,expected,description", test_cases)
    @allure.title("注册测试: {description}")
    def test_registration_cases(self, username, password, email, expected, description):
        """参数化注册测试"""

        with allure.step(f"测试场景: {description}"):
            print(f"用户名: {username}, 密码长度: {len(password)}")

        with allure.step("执行注册验证"):
            validation_result = self.validate_registration(username, password, email)

            # 记录验证详情
            validation_details = f"""
            用户名验证: {'通过' if validation_result['username_valid'] else '失败'}
            密码验证: {'通过' if validation_result['password_valid'] else '失败'} 
            邮箱验证: {'通过' if validation_result['email_valid'] else '失败'}
            总体结果: {'通过' if validation_result['overall'] else '失败'}
            """
            allure.attach(validation_details, name="验证详情",
                          attachment_type=allure.attachment_type.TEXT)

        with allure.step("验证总体结果"):
            # pytest 断言验证期望结果
            assert validation_result["overall"] == expected, (
                f"注册验证结果不符合预期: 期望 {expected}, 实际 {validation_result['overall']}"
            )

    def validate_registration(self, username, password, email):
        """模拟注册验证逻辑"""
        username_valid = len(username) >= 5
        password_valid = len(password) >= 8
        email_valid = "@" in email and "." in email

        overall = username_valid and password_valid and email_valid

        return {
            "username_valid": username_valid,
            "password_valid": password_valid,
            "email_valid": email_valid,
            "overall": overall
        }