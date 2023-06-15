
def protocol():
    count = 0
    currentBuffer = []

    with open('day6-input.txt', 'r') as f:
        for line in f.readlines():
            arrayOfChars = list(line)

            for char in arrayOfChars:
                count += 1
                currentBuffer += char
                if len(currentBuffer) == 14:
                    noMatches = check_elements(currentBuffer)
                    if noMatches is True:
                        return ('no match', count, currentBuffer)
                    currentBuffer.remove(currentBuffer[0])

def check_elements(currentBuffer):
    for item in currentBuffer:
        newList = currentBuffer.copy()
        newList.remove(item)
        for i in newList:
            if item is i:
                return False
    return True


puzzleAnswer = protocol()
print(puzzleAnswer)
