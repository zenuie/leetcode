# Given a binary tree, determine if it is height-balanced.
#
#  For this problem, a height-balanced binary tree is defined as:
#
#
#  a binary tree in which the left and right subtrees of every node differ in he
# ight by no more than 1.
#
#
#
#  Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
#  Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
#  Example 3:
#
#
# Input: root = []
# Output: true
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 5000].
#  -104 <= Node.val <= 104
#
#  Related Topics Tree Depth-first Search Recursion
#  👍 3592 👎 235


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root):
            if not root:
                return 0, 1
            left, result_left = dfs(root.left)
            right, result_right = dfs(root.right)
            if result_left and result_right and (-1 <= left - right <= 1):
                result = 1
            else:
                result = 0
            return max(left, right) + 1, result

        return dfs(root)[1] == 1

# leetcode submit region end(Prohibit modification and deletion)
