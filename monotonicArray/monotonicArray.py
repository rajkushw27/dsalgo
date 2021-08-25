def isMonotonic(array):
    increasing = True
    decreasing = True

    for i in range(1, len(array)):

        if array[i] < array[i-1]:
            decreasing = False
        if array[i] > array[i-1]:
            increasing = False

    return decreasing or increasing


print(isMonotonic([1, 2, 3, 45, 56]))
