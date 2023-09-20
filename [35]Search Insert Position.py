def searchInsert(nums, target):
    nums.append(target)
    return sorted(nums).index(target)


searchInsert([1,3,5,6],5)