def maxSubArray(nums):
    if max(nums) <= 0: return nums[0]
    sum = 0
    max_sum = nums[0]
    for i in range(len(nums)):
        sum += nums[i]
        sum = max(0, sum)
        max_sum = max(sum, max_sum)
    print(max_sum)


maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
