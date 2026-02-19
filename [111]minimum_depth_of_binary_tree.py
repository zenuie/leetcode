def minDepth(self, root):
    if not root:
        return 0
    if not root.left or not root.right:
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    else:
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

