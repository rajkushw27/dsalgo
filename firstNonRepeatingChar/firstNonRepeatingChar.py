def firstNonRepeatingCharacter(string):
    characterCount = {}

    for char in string:
        characterCount[char] = characterCount.get(char, 0) + 1

    for idx in range(len(string)):
        char = string[idx]
        if characterCount[char] == 1:
            return idx
        return -1
