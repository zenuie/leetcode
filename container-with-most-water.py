class Solution:
    def maxArea(self, height: List[int]) -> int:
        lst = [0]
        for i in range(len(height)):
            if height[0] < height[-1]:
                lst.append(height[0] * (len(height) - 1))
                del height[0]

            elif height[0] > height[-1]:
                lst.append(height[-1] * (len(height) - 1))
                del height[-1]

            else:
                lst.append(height[-1] * (len(height) - 1))
                del height[-1]
        return max(lst)
