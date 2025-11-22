import pytest
import json
import allure
import requests

from Project_2025_10.RPlan.basic_request import response


@allure.feature("用户管理")
class Test_UserCRUD():
    userId_list = None
    @allure.story("新建用户")
    @allure.title("新建用户")
    def test_createUser(self,user_data):
        with allure.step("获取请求响应"):
            data = {
                'username': user_data['username'],
                'password': user_data['password'],
                'email': user_data['email'],
            }
            response = requests.post('http://api.example.com/users', json=data)
            response_json = json.loads(response.text)
            allure.attach(response_json,name="用户创建返回内容",attachment_type=allure.attachment_type.JSON)

        with allure.step("验证响应"):
            if response.status_code in (200,201):
                Test_UserCRUD.userId_list = response_json['user_id']

    @allure.story("ID查询用户")
    @allure.title("ID查询用户")
    def test_getUser(self):
        with allure.step("ID查询"):
            response = requests.get(f'http://api.example.com/users/{Test_UserCRUD.userId_list}')
            response_json = json.loads(response.text)
            allure.attach(response_json, name="用户查询返回内容", attachment_type=allure.attachment_type.JSON)

        with allure.step("返回验证"):
            assert response.status_code == 200
            assert response_json['user_id'] == Test_UserCRUD.userId_list

    @allure.story("ID更改用户信息")
    @allure.title("ID更改用户信息")
    def test_updateUser(self):
        with allure.step("提交修改信息"):
            data_new = {
                'username' : 'new'
            }
            response = requests.put('http://api.example.com/users/{user_id}'.format(user_id = Test_UserCRUD.userId_list), json=data_new)
            response_json = json.loads(response.text)
            allure.attach(response_json,name="用户更改返回内容",attachment_type=allure.attachment_type.JSON)

        with allure.step("验证修改是否成功"):
            assert response.status_code == 200
            assert response_json['user_id'] == Test_UserCRUD.userId_list
            assert response_json['username'] == 'new'

    @allure.story("ID删除用户信息")
    @allure.title("ID删除用户信息")
    def test_deleteUser(self):
        with allure.step("提交删除信息"):
            response = requests.delete(f'http://api.example.com/users/{Test_UserCRUD.userId_list}')
            response_json = json.loads(response.text)
            allure.attach(response_json, name="用户删除返回内容", attachment_type=allure.attachment_type.JSON)

        with allure.step("验证删除是否成功"):
            assert response.status_code in (200,201)
            assert response_json['user_id'] == Test_UserCRUD.userId_list

        with allure.step("再次访问验证"):
            response = requests.get(f'http://api.example.com/users/{Test_UserCRUD.userId_list}')
            assert response.status_code == 404