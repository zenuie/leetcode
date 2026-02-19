def preorder(self, root: 'Node') -> List[int]:
    if not root: return None
    result = [root.val]
    for i in root.children:
        result += self.preorder(i)
    return result
