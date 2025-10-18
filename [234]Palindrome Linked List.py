from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        asc = ""
        desc = ""
        while head != None:
            asc += str(head.val)
            desc = str(head.val) + desc
            head = head.next
        return asc == desc
