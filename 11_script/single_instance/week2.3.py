class SingletonConfig:
    # 1. 定义类变量，用于存储唯一的实例
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        # 2. 请在这里写判断逻辑
        if cls._instance is None:
            # 提示：创建新对象的语法是 super().__new__(cls)
            cls._instance = super().__new__(cls)

            # 3. 返回那个唯一的实例
        return cls._instance

    def __init__(self):
        if not self._initialized:
            print("初始化 Config...")
            self._initialized = True
        else:
            return


if __name__ == "__main__":
    c1 = SingletonConfig()
    c2 = SingletonConfig()
    print(c1 is c2)
