import requests
from typing import Dict, Optional
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class AuthClient:
    def __init__(self, host: str = "http://httpbin.org"):
        self.host = host
        self.session = requests.session()

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

    def login(self, username: str, password: str) -> Optional[Dict]:
        data = {"username": username, "password": password}
        res = self.send_request("post", "/post", data=data)
        # 假token
        if res.status_code == "200":
            self.session.headers.update({"Authorization": "Bearer abc-123-token"})

    def get_headers(self):
        res = self.send_request("get", "/headers")
        print(res)
