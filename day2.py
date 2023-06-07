def rpsResult(playKey):
    win = ['AZ', 'BZ', 'CZ']
    tie = ['AY', 'BY', 'CY']
    lose = ['AX', 'BX', 'CX']

    if playKey in win:
        return 6
    elif playKey in tie:
        return 3
    elif playKey in lose:
        return 0


def choiceResult(playKey):
    x = ['AY', 'BX', 'CZ']
    y = ['AZ', 'BY', 'CX']
    z = ['AX', 'BZ', 'CY']

    if playKey in x:
        return 1
    elif playKey in y:
        return 2
    elif playKey in z:
        return 3


def createScores():
    currentScore = 0

    with open('day2-input.txt', 'r') as f:
        for line in f.readlines():
            playKey = line[0] + line[2]
            roundScore = rpsResult(playKey) + choiceResult(playKey)
            currentScore += roundScore
            print(rpsResult(playKey), choiceResult(playKey), playKey)
    return currentScore


totalScore = createScores()
print(totalScore)
