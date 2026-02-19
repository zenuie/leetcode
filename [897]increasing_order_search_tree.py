class Solution:
    def increasingBST(self, root: TreeNode,tail=None) -> TreeNode:
        node = root
        if not root:
            return tail
        result = self.increasingBST(node.left,root)
        node.left = None
        node.right = self.increasingBST(node.right,tail)
        return result