from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
        该函数可通过输入整数列表、目标值，返回符合目标值的数字的下表
    Args:
        数字列表，目标值

    Returns:
        目标数字下表
    """
    nums_dict = {}
    for index, num in enumerate(nums):
        if target - num in nums_dict:
            return [nums_dict[target - num], index]
        nums_dict[num] = index
    raise ValueError
