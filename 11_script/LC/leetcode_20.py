from operator import index
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            need = target - num
            if need in hash_map:
                return [hash_map[need], index]
            else:
                hash_map[num] = index
        return []


class Solution:
    def isValid(self, s: str) -> bool:
        # 1. 建立映射表：key是右括号，value是左括号
        # 这样做的好处是，如果以后增加了 <>，只需要改这里，不需要改下面的逻辑
        pairs = {")": "(", "]": "[", "}": "{"}

        # Python 中，直接用 List 作为 Stack 即可，不需要引入 deque
        # List 的 append() 和 pop() 都是 O(1) 的
        stack = []

        for char in s:
            # 如果字符在字典的 key 里（说明是右括号）
            if char in pairs:
                # 栈为空 或者 栈顶元素不匹配
                if not stack or stack[-1] != pairs[char]:
                    return False
                # 匹配成功，弹出栈顶
                stack.pop()
            else:
                # 说明是左括号，直接入栈
                stack.append(char)

        # 2. 简洁的返回：如果 stack 为空(False)，则返回 True
        return not stack
