def protocol():
    count = 0
    currentBuffer = []
    noMatchStreak = []

    with open('day6-input.txt', 'r') as f:
        for line in f.readlines():
            arrayOfChars = list(line)

            for char in arrayOfChars:
                count += 1
                currentBuffer += char
                noMatchStreak.append(check_elements(currentBuffer))

                if len(currentBuffer) == 4:
                    if noMatchStreak == [False, False, False, False]:
                        return ('no match', (count - 3), currentBuffer)
                    else:
                        noMatchStreak.remove(noMatchStreak[0])
                    currentBuffer.remove(currentBuffer[0])


def check_elements(l):
    element = l[0]
    newList = l.copy()
    newList.remove(newList[0])
    x = False
    for i in newList:
        if element is i:
            x = True
    return x


puzzleAnswer = protocol()
print(puzzleAnswer)
