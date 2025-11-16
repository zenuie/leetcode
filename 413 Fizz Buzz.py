from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzbuzz_list = [
            "FizzBuzz" if i % 15 == 0 else  # 情況 1: 兩者皆可整除
            "Fizz" if i % 3 == 0 else  # 情況 2: 僅可被 3 整除
            "Buzz" if i % 5 == 0 else  # 情況 3: 僅可被 5 整除
            str(i)  # 情況 4: 兩者皆不可整除，輸出數字本身
            for i in range(1, n + 1)
        ]
        return fizzbuzz_list


test = Solution()
print(test.fizzBuzz(15))
