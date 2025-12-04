import yaml
import os


def load_yaml_data(file_path):
    """
    读取 YAML 文件并返回 Python 对象
    :param file_path: 相对于项目根目录的文件路径，例如 'data/users.yaml'
    """
    # 获取当前脚本所在目录的上一级目录（即 week_7 根目录）
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, file_path)

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"读取 YAML 文件失败: {e}")
        return []


if __name__ == "__main__":
    # 调试一下，看看能不能读出来
    print(load_yaml_data("data/users.yaml"))
