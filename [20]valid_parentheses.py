class Solution:
    def isValid(self, s: str) -> bool:

        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack_list = []
        for char in s:
            if char in bracket_map.values():
                stack_list.append(char)

            elif char in bracket_map.keys():
                if len(stack_list) == 0 or bracket_map.get(char) != stack_list.pop():
                    return False
        return not stack_list


test = Solution()
print(test.isValid("{{}"))
