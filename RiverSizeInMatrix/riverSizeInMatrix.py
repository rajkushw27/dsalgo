def riverSizes(matrix):
    riverSize = []
    visitedNode = [[False for value in row]for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if visitedNode[i][j]:
                continue
            traverseNode(i, j, matrix, visitedNode, riverSize)

    return riverSize


def traverseNode(i, j, matrix, visitedNode, riverSize):
    currentRiverSize = 0

    nodeToTraverse = [[i, j]]

    while len(nodeToTraverse):
        currentNode = nodeToTraverse.pop()

        i = currentNode[0]
        j = currentNode[1]

        if visitedNode[i][j]:
            continue

        visitedNode[i][j] = True

        if matrix[i][j] == 0:
            continue

        currentRiverSize += 1
        neighbourNode = findNeighbourNodes(i, j, matrix, visitedNode)

        for neighbour in neighbourNode:
            nodeToTraverse.append(neighbour)

    if currentRiverSize > 0:
        riverSize.append(currentRiverSize)


def findNeighbourNodes(i, j, matrix, visitedNode):
    unVisitedNeighbour = []
    if i > 0 and not visitedNode[i-1][j]:
        unVisitedNeighbour.append([i-1, j])
    if i < len(matrix) - 1 and not visitedNode[i+1][j]:
        unVisitedNeighbour.append([i+1, j])
    if j > 0 and not visitedNode[i][j-1]:
        unVisitedNeighbour.append([i, j-1])
    if j < len(matrix[i])-1 and not visitedNode[i][j+1]:
        unVisitedNeighbour.append([i, j+1])

    return unVisitedNeighbour
