scoreKey = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        'A': 27,
        'B': 28,
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52
}


def commonItem(splitLists):
    listA = splitLists[0]
    listB = splitLists[1]
    listC = splitLists[2]
    matchAB = set(listA).intersection(listB)
    matchAC = set(listA).intersection(listC)
    matchABC = set(matchAC).intersection(matchAB)
    cleanValue = remove_items(matchABC, '\n')
    return cleanValue


def remove_items(test_list, item):

    res = [i for i in test_list if i != item]

    return res


def scoreItem(match):
    return scoreKey[match.pop()]


def createScores():
    currentScore = 0
    groupCount = 0
    groupValues = []
    with open('day3-input.txt', 'r') as f:
        for line in f.readlines():
            groupCount += 1
            groupValues.append(line)
            if groupCount == 3:
                matchedValue = commonItem(groupValues)
                score = scoreItem(matchedValue)

                groupCount = 0
                groupValues.clear()

                currentScore += int(score)
    return currentScore


totalScore = createScores()
print(totalScore)
