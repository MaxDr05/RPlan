# test_simple.py
import allure
import pytest


# 用 @allure.feature 标记这个测试属于什么功能
@allure.feature("计算器功能")
class TestCalculator:

    # 用 @allure.story 标记具体的用户故事
    @allure.story("加法运算")
    def test_addition(self):
        """测试加法功能"""
        # 用 with allure.step 记录测试步骤
        with allure.step("准备测试数据"):
            a = 5
            b = 3

        with allure.step("执行加法运算"):
            result = a + b

        with allure.step("验证计算结果"):
            assert result == 8
            print(f"计算结果: {a} + {b} = {result}")