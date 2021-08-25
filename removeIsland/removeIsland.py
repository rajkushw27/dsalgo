def removeIslands(matrix):
    onesConnectedToBorder = [[False for col in matrix[0]] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder

            if not isBorder:
                continue
            if matrix[row][col] != 1:
                continue

            findOneConnectedToBorder(matrix, row, col, onesConnectedToBorder)

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if onesConnectedToBorder[row][col] == True:
                continue

            matrix[row][col] = 0
    return matrix


def findOneConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
    stack = [(startRow, startCol)]
    while len(stack) > 0:
        currentPosition = stack.pop()
        currRow, currCol = currentPosition

        alreadyVisited = onesConnectedToBorder[currRow][currCol]
        if alreadyVisited:
            continue

        onesConnectedToBorder[currRow][currCol] = True

        neighbors = getNeighbors(matrix, currRow, currCol)

        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue
            stack.append(neighbor)


def getNeighbors(matrix, row, col):
    neighbor = []

    rowLen = len(matrix)
    colLen = len(matrix[row])

    if row - 1 >= 0:
        neighbor.append((row - 1, col))
    if row + 1 < rowLen:
        neighbor.append((row + 1, col))
    if col - 1 >= 0:
        neighbor.append((row, col - 1))
    if col + 1 < colLen:
        neighbor.append((row, col + 1))
    return neighbor


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]


print(removeIslands(matrix))
