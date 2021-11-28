class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findMaxUtil(node):
    if node is None:
        return 0
    
    l = findMaxUtil(node.left)
    r = findMaxUtil(node.right)
    
    max_single = max(max(l, r) + node.data, node.data)
    max_top = max(max_single, l + r + node.data)
    
    findMaxUtil.res = max(findMaxUtil.res, max_top)
    return max_single


def findMaxSum(node):
    findMaxUtil.res = float('-inf')
    findMaxUtil(node)
    return findMaxUtil.res


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    print(findMaxSum(root))
    