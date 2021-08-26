def firstNonRepeatingCharacter(string):
    for idx in range(len(string)):
        duplicate = False
    for idx2 in range(len(string)):
        if string[idx] == string[idx2] and idx != idx2:
            duplicate = True

    if not duplicate:
        return idx
    return -1
