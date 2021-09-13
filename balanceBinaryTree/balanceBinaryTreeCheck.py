class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo():

    def __init__(self, isBalance, height):
        self.height = height
        self.isBalance = isBalance


def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalance


def getTreeInfo(Node):
    if Node == None:
        return TreeInfo(True, -1)

    getLeftSubTreeInfo = getTreeInfo(Node.left)
    getRightSubTreeInfo = getTreeInfo(Node.right)

    isBalance = (getLeftSubTreeInfo.isBalance and getRightSubTreeInfo.isBalance and abs(
        getRightSubTreeInfo.height - getLeftSubTreeInfo.height) <= 1)
    height = max(getLeftSubTreeInfo.height, getRightSubTreeInfo.height) + 1

    return TreeInfo(isBalance, height)
