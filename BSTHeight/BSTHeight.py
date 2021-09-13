class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(Node):
    if Node is None:
        return 0

    else:

        lmaxDepth = maxDepth(Node.left)
        rmaxDepth = maxDepth(Node.right)

        return lmaxDepth+1 if lmaxDepth > rmaxDepth else rmaxDepth + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print(f"Height of tree is {maxDepth(root)}")
