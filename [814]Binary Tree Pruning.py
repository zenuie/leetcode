def prune_helper(self, node: TreeNode):
    '''
    Input: one node as root node of binary tree
    Output: Repeat remove all leaf node whose value is 0 until all leaf nodes is non-zero
    '''

    if not node:
        # base case:
        # empty node or empty tree
        return True

    # pre-order DFS down to next level
    left_removal = self.prune_helper(node.left)
    right_removal = self.prune_helper(node.right)

    if left_removal and right_removal and node.val == 0:
        # update node as prune target by return True
        return True

    if left_removal:
        # prune left leaf node
        node.left = None

    if right_removal:
        # prune right leaf node
        node.right = None

    # node is either a non-leaf node, or a leaf node with 1
    return False


def pruneTree(self, root: TreeNode) -> TreeNode:
    if self.prune_helper(root):
        # root is either empty node naturally, or pruned finally.
        return None
    else:
        # root still exists eventually
        return root