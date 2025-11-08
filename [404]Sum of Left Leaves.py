from typing import Optional

from tree import build_tree, print_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """前序遍歷：root -> left -> right"""

        # 判斷是否為葉節點：存在且沒有左右子
        def is_leaf(node: Optional['TreeNode']) -> bool:
            return node is not None and node.left is None and node.right is None

        if root is None:
            return 0

        total = 0

        # 在父節點檢查左孩子是否為「左葉」
        if is_leaf(root.left):
            total += root.left.val

        # 繼續往左右子樹遞迴，累加各自的「左葉」總和
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)

        return total


def run_case(level_order):
    root = build_tree(level_order)
    print("輸入樹（層序）:")
    print_tree(root)

    sol = Solution()
    ans = sol.sumOfLeftLeaves(root)
    print(f"答案: {ans}\n")


if __name__ == "__main__":
    # 範例 1：期望 24
    run_case([3, 9, 20, None, None, 15, 7])

    # 範例 2：期望 0
    run_case([1])

    # 常見誤判例：期望 4
    run_case([1, 2, 3, 4, 5])
