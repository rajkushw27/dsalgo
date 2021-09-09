def powerset(array, index=None):
    if index is None:
        index = len(array) - 1
    if index < 0:
        return [[]]

    element = array[index]
    subset = powerset(array, index-1)

    for i in range(len(subset)):
        currentSubSet = subset[i]
        subset.append(currentSubSet + [element])

    return subset


print(powerset([1, 2, 3, 4]))
