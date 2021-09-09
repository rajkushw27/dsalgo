def powerset(array):
    subSet = [[]]

    for element in array:
        for i in range(len(subSet)):
            currentSubSet = subSet[i]
            subSet.append(currentSubSet + [element])
    return subSet


print(powerset([1, 2, 3, 4]))
