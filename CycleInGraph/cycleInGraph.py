def cycleInGraph(edges):
    numberOfNodes = len(edges)
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if visited[node]:
            continue

        cycleCheck = isCycle(edges, node, visited, currentlyInStack)

        if cycleCheck:
            return True

    return False


def isCycle(edges, node, visited, currentlyInStack):

    visited[node] = True
    currentlyInStack[node] = True

    neighbours = edges[node]

    for neighbour in neighbours:

        if not visited[neighbour]:

            cycleCheck = isCycle(edges, neighbour, visited, currentlyInStack)
            if cycleCheck:
                return True

        if currentlyInStack[neighbour]:
            return True

    currentlyInStack[node] = False
    return False
