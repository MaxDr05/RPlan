import requests
from typing import Optional, Dict


class BaiduClient:

    def __init__(self, host: str = "https://www.baidu.com"):
        self.host = host
        self.session = requests.session()
        self.session.headers.update({"User-Agent": "Chrome/Test-Bot"})

    def search(self, keyword: str) -> Optional[Dict]:
        try:
            res = self.session.get(url=self.host, params={"keyword": keyword})
            res.raise_for_status()
            print(res.status_code)
            return res.json()
        except requests.HTTPError as he:
            print(f"HTTP请求异常：{he}")
            return None
        except requests.ConnectionError as ce:
            print(f"连接异常:{ce}")
            return None
        except Exception as e:
            print(f"特殊异常:{e}")
            return None
