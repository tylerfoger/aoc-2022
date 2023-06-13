stacks = {
        '1': ['N', 'C', 'R', 'T', 'M', 'Z', 'P'],
        '2': ['D', 'N', 'T', 'S', 'B', 'Z'],
        '3': ['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G'],
        '4': ['G', 'R', 'Z'],
        '5': ['Z', 'N', 'R', 'H'],
        '6': ['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D'],
        '7': ['W', 'D', 'Z', 'R', 'C', 'G', 'M'],
        '8': ['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q'],
        '9': ['S', 'Q', 'P', 'W', 'N']
}


def sortStack():
    count = 0
    topItems = ''
    with open('day5-input.txt', 'r') as f:
        for line in f.readlines():
            count += 1
#            if count > 13:
#                pass
            if count >= 11:
                instruction = line.split(' ')
                print(instruction)
                numberOfCratesToMove = range(0, int(instruction[1]))
                giverStack = stacks[instruction[3]]
                receiverStack = stacks[instruction[5].split('\n')[0]]

                for crates in numberOfCratesToMove:
                    print(giverStack, len(giverStack))
                    if len(giverStack) >= 1:
                        itemToGive = giverStack.pop()
                        receiverStack.append(itemToGive)

    for stack in stacks:
        topItems += stacks[stack][-1]
        print(topItems)
    return topItems


puzzleAnswer = sortStack()
print(puzzleAnswer)
