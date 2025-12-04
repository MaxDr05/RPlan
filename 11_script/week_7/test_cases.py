import pytest
import allure
from utils.yaml_loader import load_yaml_data

# 第一种格式
# 格式：("参数名1, 参数名2", [ (数据组1), (数据组2), ... ])
# @pytest.mark.parametrize(
#     "name, job",
#     [
#         ("neo", "leader"),  # 第 1 次运行用这组数据
#         ("trinity", "hacker"),  # 第 2 次运行用这组数据
#         ("morpheus", "captain"),  # 第 3 次运行用这组数据
#     ],
# )

# 第二种格式
# -------------------------------------------
# 第七周新增：数据驱动测试
# -------------------------------------------
# 定义测试数据：每组数据包含 (case_name, name, job)
# case_name 是为了让我们在报告里看清楚测的是什么场景


def get_case_name(data_row):
    return data_row[0]


# 🟢 1. 标注测试的大模块 (Feature)
@allure.feature("用户管理模块")
class TestDDT:

    # 🟢 2. 标注具体的功能点 (Story)
    @allure.story("创建用户 - 数据驱动测试")
    # 🟢 3. 标注测试的标题 (Title) - 可以引用参数
    @allure.title("测试场景: {user_data[0]}")
    @pytest.mark.parametrize(
        "user_data", load_yaml_data("data/users.yaml"), ids=get_case_name
    )
    def test_create_user_from_yaml(self, api_client, user_data):
        case_name, name, job = user_data

        # 🟢 4. 标注测试步骤 (Step) - 这会显示在报告的时间轴里
        with allure.step(f"步骤1: 使用 name={name}, job={job} 创建用户"):
            print(f"\n[YAML] 执行用例: {case_name}")
            res = api_client.create_user(name=name, job=job)

        with allure.step("步骤2: 验证响应数据"):
            assert res is not None
            assert res["json"]["name"] == name
            assert res["json"]["job"] == job
