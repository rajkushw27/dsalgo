def minNumberOfCoinsForChange(n, denoms):
    numberOfCoins = [float('inf') for i in range(n+1)]
    numberOfCoins[0] = 0

    for d in denoms:
        for amount in range(len(numberOfCoins)):
            if d <= amount:
                numberOfCoins[amount] = min(
                    numberOfCoins[amount], 1 + numberOfCoins[amount-d])

    return numberOfCoins[n] if numberOfCoins[n] != float('inf') else -1


print(minNumberOfCoinsForChange(6, [1, 2, 4]))
