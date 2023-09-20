def merge(nums1, m, nums2, n):
    while n:
        if m and nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1


"""
nums1[m:] = nums2[:n]
        nums1.sort()
"""

merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
