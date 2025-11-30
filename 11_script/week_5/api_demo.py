import sys

import requests
from requests.exceptions import ConnectionError, RequestException, Timeout

url = "https://reqres.in"


def list_user():
    url = "https://reqres.in/api/users"
    params = {"page": 2}
    try:
        response = requests.get(url=url, params=params)
        response.raise_for_status()
        print(f"响应状态码为：{response.status_code}")
        if response.status_code == 200:
            print(f"访问成功")

    except ConnectionError as ce:
        print(f"连接失败{ce}")
        sys.exit(1)
    except RequestException as re:
        print(f"请求失败:{re}")
        sys.exit(1)
    except Exception as e:
        print(f"特殊异常：{e}")
        sys.exit(1)
    finally:
        return response


def create_user():
    url = "https://reqres.in/api/users"
    headers = {"User-Agent": "Python/Test-Script"}
    json_data = {"name": "morpheus", "job": "leader"}

    try:
        response = requests.post(url=url, headers=headers, json=json_data)
        response.raise_for_status()
        print(f"响应状态码为：{response.status_code}")
        if response.status_code == 200:
            print(f"访问成功")
            print(f"{response.json()['id'],response.json()['createdAt']}")

    except ConnectionError as ce:
        print(f"连接失败{ce}")
        sys.exit(1)
    except RequestException as re:
        print(f"请求失败:{re}")
        sys.exit(1)
    except Exception as e:
        print(f"特殊异常：{e}")
        sys.exit(1)
    finally:
        return response


def update_user():
    url = "https://reqres.in/api/users/2"
    headers = {"User-Agent": "Python/Test-Script"}
    json_data = {"name": "morpheus", "job": "zion resident"}

    try:
        response = requests.put(url=url, headers=headers, json=json_data)
        response.raise_for_status()
        print(f"响应状态码为：{response.status_code}")
        if response.status_code == 200:
            print(f"访问成功")

    except ConnectionError as ce:
        print(f"连接失败{ce}")
        sys.exit(1)
    except RequestException as re:
        print(f"请求失败:{re}")
        sys.exit(1)
    except Exception as e:
        print(f"特殊异常：{e}")
        sys.exit(1)
    finally:
        return response


def delete_user():
    url = "https://reqres.in/api/users/2"
    try:
        response = requests.delete(url=url)
        response.raise_for_status()
        print(f"响应状态码为：{response.status_code}")

    except ConnectionError as ce:
        print(f"连接失败{ce}")
        sys.exit(1)
    except RequestException as re:
        print(f"请求失败:{re}")
        sys.exit(1)
    except Exception as e:
        print(f"特殊异常：{e}")
        sys.exit(1)
    finally:
        return response
