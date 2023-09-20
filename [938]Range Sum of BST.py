class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return
            if low <= root.val <= high:
                self.res += root.val
            if low <= root.val:
                dfs(root.left)
            if high >= root.val:
                dfs(root.right)

        self.res = 0
        dfs(root)
        return self.res
