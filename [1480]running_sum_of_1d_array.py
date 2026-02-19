def runningSum(nums):
    result = []
    temp = 0
    for i in nums:
        temp += i
        result.append(temp)


runningSum([1, 2, 3, 4])
