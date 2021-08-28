def firstDuplicateValue(array):

    minimumSecondIndex = len(array)

    for idx, num in enumerate(array):
        for j in range(idx+1, len(array)):
            if array[j] == num:
                minimumSecondIndex = min(minimumSecondIndex, j)

    if minimumSecondIndex == len(array):
        return -1

        return array[minimumSecondIndex]
