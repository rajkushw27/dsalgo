def minimumCharactersForWords(words):

    maximumFrequencyCharacterSet = {}

    for word in words:
        characterFrequencies = countCharacterFrequency(word)
        updateMaximumFrequency(characterFrequencies,
                               maximumFrequencyCharacterSet)
    return makeArrayFromCharacterSet(maximumFrequencyCharacterSet)


def countCharacterFrequency(word):
    characterFrequency = {}

    for w in word:
        characterFrequency[w] = characterFrequency.get(w, 0) + 1
    return characterFrequency


def updateMaximumFrequency(characterFrequencies, maximumFrequency):

    for character in characterFrequencies:
        maximumFrequency[character] = max(
            characterFrequencies[character], maximumFrequency.get(character, 0))

    return maximumFrequency


def makeArrayFromCharacterSet(maximumFrequencyCharacterSet):

    characters = []

    for character in maximumFrequencyCharacterSet:

        frequency = maximumFrequencyCharacterSet[character]

        for _ in range(frequency):
            characters.append(character)

    return characters


print(minimumCharactersForWords(["this", "is", "natural!", "view", "deed"]))
