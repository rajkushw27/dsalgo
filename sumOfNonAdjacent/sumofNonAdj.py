array = [75, 105, 120, 75, 90, 135]


def sumOfNonAdj(array):

    maxSumArray = array[:]
    maxSumArray[1] = max(array[0], array[1])
    for index in range(2, len(array)):
        maxSumArray[index] = max(maxSumArray[index-1],
                                 maxSumArray[index-2]+array[index])

    return maxSumArray[-1]


sumOfNonAdj(array)
