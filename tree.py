# tree.py

from typing import Optional, List, Union
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(level_order: List[Union[int, None]]) -> Optional[TreeNode]:
    """
    依照 LeetCode 的 level-order（層序）陣列建構二元樹。
    例如: [3,9,20,None,None,15,7]
    規則：None 表示該位置沒有節點。
    """
    if not level_order:
        return None

    it = iter(level_order)
    root_val = next(it)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    queue = deque([root])

    for val_left, val_right in zip(it, it):
        node = queue.popleft()
        if val_left is not None:
            node.left = TreeNode(val_left)
            queue.append(node.left)
        if val_right is not None:
            node.right = TreeNode(val_right)
            queue.append(node.right)

    # 若 level_order 長度為奇數，會剩下一個最後的 left 值
    try:
        leftover = next(it)
        node = queue.popleft()
        if leftover is not None:
            node.left = TreeNode(leftover)
            queue.append(node.left)
    except StopIteration:
        pass

    return root


def print_tree(root: Optional[TreeNode]) -> None:
    """
    以層序列印樹，方便除錯觀察。
    輸出形式為每層的節點值（None 代表空）。
    """
    if not root:
        print("[]")
        return

    queue = deque([root])
    out = []
    while queue:
        node = queue.popleft()
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)

    # 去除尾端多餘的 None，讓輸出更精簡
    while out and out[-1] is None:
        out.pop()

    print(out)
