def makeSectionList(assignments):
    start = int(assignments[0])
    end = int(assignments[1])
    listOfSections = []
    for section in range(start, end + 1):
        listOfSections.append(section)
    return listOfSections


def fullyContainedPairs():
    listOfPairs = 0
    with open('day4-input.txt', 'r') as f:
        for line in f.readlines():
            splitLines = line.split(',')
            elf1 = makeSectionList(splitLines[0].split('-'))
            elf2 = makeSectionList(splitLines[1].split('-'))

            sameSections = set(elf1).intersection(elf2)
            if len(sameSections) > 0:
                listOfPairs += 1
            else:
                pass
    return listOfPairs


totalPairs = fullyContainedPairs()
print(totalPairs)
