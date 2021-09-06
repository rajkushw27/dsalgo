class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    array = []
    inOrderTraversal(tree, array)
    return array[len(array) - k]


def inOrderTraversal(tree, array):
    if tree is None:
        return
    inOrderTraversal(tree.left, array)
    array.append(tree.value)
    inOrderTraversal(tree.right, array)
