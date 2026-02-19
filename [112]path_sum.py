# Given the root of a binary tree and an integer targetSum, return true if the t
# ree has a root-to-leaf path such that adding up all the values along the path eq
# uals targetSum.
#
#  A leaf is a node with no children.
#
#
#  Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
#
#
#  Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
#
#
#  Example 3:
#
#
# Input: root = [1,2], targetSum = 0
# Output: false
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 5000].
#  -1000 <= Node.val <= 1000
#  -1000 <= targetSum <= 1000
#
#  Related Topics Tree Depth-first Search
#  👍 3200 👎 620


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return None
        queue = deque()
        queue.append((root, root.val))
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right and path == targetSum: return True
            if node.left: queue.append((node.left, path + node.left.val))
            if node.right: queue.append((node.right, path + node.right.val))
        return False
# leetcode submit region end(Prohibit modification and deletion)
