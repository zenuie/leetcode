# Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
#  symmetric around its center).
#
#
#  Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
#
#  Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 1000].
#  -100 <= Node.val <= 100
#
#
#
# Follow up: Could you solve it both recursively and iteratively? Related Topics
#  Tree Depth-first Search Breadth-first Search
#  👍 6236 👎 165


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.mirror(root, root)

    def mirror(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.mirror(p.left, q.right) and self.mirror(p.right, q.left)
# leetcode submit region end(Prohibit modification and deletion)
