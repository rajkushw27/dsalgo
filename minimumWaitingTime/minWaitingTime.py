def minimumWaitingTime(queries):
    totalWaitingTime = 0
    queries.sort()

    for idx, time in enumerate(queries):
        queriesLeft = len(queries) - (idx+1)
        totalWaitingTime += time*queriesLeft
    return totalWaitingTime
