# Given the root of a binary tree, return the inorder traversal of its nodes' va
# lues.
#
#
#  Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
#
#  Example 2:
#
#
# Input: root = []
# Output: []
#
#
#  Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
#  Example 4:
#
#
# Input: root = [1,2]
# Output: [2,1]
#
#
#  Example 5:
#
#
# Input: root = [1,null,2]
# Output: [1,2]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 100].
#  -100 <= Node.val <= 100
#
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively? Related
#  Topics Hash Table Stack Tree
#  👍 4789 👎 219


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.inorder(root, result)
        return result

    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)
# leetcode submit region end(Prohibit modification and deletion)
