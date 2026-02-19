def postorder(self, root: 'Node') -> List[int]:
    if not root: return None
    result = []
    for i in root.children:
        result += self.postorder(i)
    result.append(root.val)

    return result