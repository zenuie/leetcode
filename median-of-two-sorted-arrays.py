class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = sorted(nums2 + nums1)
        longLst = len(lst)
        if longLst%2 ==0:
            return float((lst[longLst//2]+lst[longLst//2-1])/2)
        elif longLst%2 == 1:
            return float(lst[longLst//2])