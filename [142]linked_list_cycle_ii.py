# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 建立無環的 linked list，回傳 head
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


# 建立有環的 linked list
# pos: 環開始的 index（0-based），如果是 -1 表示沒有環（跟 LeetCode 題目一樣的定義）
def build_cycle_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    cycle_entry = None

    if pos == 0:
        cycle_entry = head

    for i, v in enumerate(values[1:], start=1):
        node = ListNode(v)
        cur.next = node
        cur = node
        if i == pos:
            cycle_entry = node

    if pos != -1:
        cur.next = cycle_entry  # 接回去形成環

    return head, cycle_entry  # 回傳 head 跟「預期的環起點」


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


# 資測
def test_detectCycle():
    s = Solution()

    # Case 1: 空鏈結
    head = None
    assert s.detectCycle(head) is None

    # Case 2: 單一節點，無環
    head = build_list([1])
    assert s.detectCycle(head) is None

    # Case 3: 單一節點，有環
    node = ListNode(1)
    node.next = node
    assert s.detectCycle(node) is node

    # Case 4: 多節點，無環
    head = build_list([1, 2, 3, 4])
    assert s.detectCycle(head) is None

    # Case 5: 多節點，環從中間開始 (例: 3->2->0->-4->2, 5 指向 2)
    head, entry = build_cycle_list([3, 2, 0, -4], pos=1)
    assert s.detectCycle(head) is entry

    # Case 6: 多節點，環從頭開始 (例: 1->2->3->4, 4 指向 1)
    head, entry = build_cycle_list([1, 2, 3, 4], pos=0)
    assert s.detectCycle(head) is entry

    print("all tests passed")


test_detectCycle()
