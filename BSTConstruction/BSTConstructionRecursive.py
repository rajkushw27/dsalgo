
class BST:
    def __init__(self, value):

        self.right = None
        self.left = None
        self.value = value


def insert(self, value):

    if value < self.value:
        if self.left is None:
            self.left = BST(value)
        else:
            self.left.insert(value)

    else:
        if self.right is None:
            self.right = BST(value)
        else:
            self.right.insert(value)
    return self


def contains(self, value):

    if value < self.value:
        if self.left is None:
            return False
        else:
            self.left.contains(value)
    elif value >= self.value:
        if self.right is None:
            return False
        else:
            self.right.contains(value)

    else:
        return True
