array = [75, 105, 120, 75, 90, 135]


def sumOfNonAdj(array):

    if not len(array):
        return 0
    if len(array) == 1:
        return array[0]

    first_max = array[0]
    second_max = max(array[0], array[1])

    for index in range(2, len(array)):
        current = max(second_max, first_max+array[index])
        first_max = second_max
        second_max = current

    return second_max


print(sumOfNonAdj(array))
