intervals = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
]


def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    # print(sortedIntervals)

    currentInterval = sortedIntervals[0]
    mergedIntervals = []
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(nextIntervalEnd, currentIntervalEnd)

        else:
            mergedIntervals.append(nextInterval)
            currentInterval = nextInterval

    return mergedIntervals


print(mergeOverlappingIntervals(intervals))
