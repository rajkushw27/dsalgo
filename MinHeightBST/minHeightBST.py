class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def minHeightBst(array):
    return constructMinHeightBST(array, 0, len(array)-1)


def constructMinHeightBST(array, leftIndex, rightIndex):

    if rightIndex < leftIndex:
        return None

    midIndex = (rightIndex + leftIndex) // 2

    bst = BST(array[midIndex])
    bst.left = constructMinHeightBST(array, leftIndex, midIndex-1)
    bst.right = constructMinHeightBST(array, midIndex+1, rightIndex)

    return bst


# Given array is sorted
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
print(minHeightBst(array))
