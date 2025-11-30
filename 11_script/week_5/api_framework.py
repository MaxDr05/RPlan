import logging
import requests
from typing import Optional, Dict, Any

# 设置日志（沿用你上一节学到的好习惯）
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class ReqresClient:
    def __init__(self, host: str = "https://reqres.in"):
        """
        初始化方法：每次实例化这个类，都会执行这里
        """
        self.host = host
        # 核心知识点：创建一个 Session 对象
        self.session = requests.Session()
        # 模拟：给所有请求加上默认 Header，比如 User-Agent
        self.session.headers.update({"User-Agent": "Python/Test-Dev-Week5"})

    def send_request(self, method: str, path: str, **kwargs) -> Optional[Dict]:
        """
        核心漏斗方法：所有接口请求都必须经过这里。
        在这里统一处理 URL 拼接、异常捕获、日志记录。
        """
        url = f"{self.host}{path}"
        try:
            # 注意：这里我们用 self.session 来发送请求，而不是 requests
            logging.info(f"正在请求: {method} {url}")
            response = self.session.request(method, url, **kwargs, timeout=10)

            # 统一的状态码检查（这里可以根据业务调整，比如统一检查 401）
            response.raise_for_status()

            # 如果是 DELETE 请求，通常没有内容，直接返回空字典或特定标识
            if method.upper() == "DELETE":
                return {"status": "deleted"}

            return response.json()

        except requests.exceptions.RequestException as e:
            logging.error(f"请求失败: {e}")
            return None
        except ValueError:
            logging.error("响应解析失败，非 JSON 格式")
            return None

    # 接上面的代码...

    def list_users(self, page: int = 1) -> Optional[Dict]:
        # 只需要关注业务：路径是什么？参数是什么？
        return self.send_request("GET", "/api/users", params={"page": page})

    def create_user(self, name: str, job: str) -> Optional[Dict]:
        # 只需要关注业务：传什么数据？
        payload = {"name": name, "job": job}
        return self.send_request("POST", "/api/users", json=payload)

    # 留给你做作业：请按照这个模式，把 update_user 和 delete_user 补充完整
    def update_user(self, uid: int, name: str, job: str) -> Optional[Dict]:
        payload = {"name": name, "job": job}
        return self.send_request("put", f"/api/users/{uid}", json=payload)

    def delete_user(self, uid: int) -> None:
        return self.send_request("delete", f"/api/users/{uid}")


if __name__ == "__main__":
    Client = ReqresClient()
    # 查询第二页
    res_search = Client.list_users(page=2)
    print(res_search)

    # 创建一个新用户
    res_create = Client.create_user(name="calvin", job="softwareEngineer")
    print(res_create)

    # 修改一个新用户
    res_update = Client.update_user(name="calvin", job="QA")
    print(res_update)

    # 删除用户
    res_delete = Client.delete_user(name="calvin")
    print(res_delete)
