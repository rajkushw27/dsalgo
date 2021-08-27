def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    possibleTotalSpeed = 0

    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest:
        blueShirtSpeeds.reverse()

    for idx in range(len(redShirtSpeeds)):
        possibleTotalSpeed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
        return possibleTotalSpeed
