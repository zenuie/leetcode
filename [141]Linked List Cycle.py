class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


s = Solution()
s.hasCycle([3, 2, 0, -4], 1)
