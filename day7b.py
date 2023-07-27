import re

hardDrive = {
    '/': {}
}
path = []
allDirectoryItems = {}
paths = ['/']
hdSize = 0
possibleAnswers = {}


def buildFileSystem(hardDrive):
    pathHistory = {}
    currentDir = hardDrive
    with open('day7-input.txt', 'r') as input:
        for line in input.readlines():
            parsedText = re.split(r' |\n', line)
            parsedText.remove('')
            if parsedText[0] == '$':
                command = parsedText[1]
                if command == 'ls':
                    pass
                elif command == 'cd':
                    location = parsedText[2]
                    if location == '..':
                        del path[-1]
                        currentDir = selectDir(path, currentDir)
                    else:
                        path.append(location)
                        currentDir = currentDir[path[-1]]
                    currentPath = path.copy()
                    pathHistory[path[-1]] = currentPath
                else:
                    pass
            elif parsedText[0] == 'dir':
                dir = parsedText[1]
                paths.append(''.join(path) + dir)
                currentDir[dir] = {}
            else:
                file = parsedText[1]
                fileName = ''.join(path) + file
                fileSize = parsedText[0]
                allDirectoryItems[fileName] = fileSize

    return hardDrive


def selectDir(path, currentDir):
    currentDir = hardDrive
    for key in path:
        currentDir = currentDir[key]
    return currentDir


fullHardDrive = buildFileSystem(hardDrive)

for path in paths:
    dirSize = 0
    pattern = re.compile(path)
    for item in allDirectoryItems:
        search = pattern.search(item)
        try:
            search.group()
            dirSize += int(allDirectoryItems[item])
        except:
            pass
    if (dirSize >= 528671) and (dirSize <= 600000):
        possibleAnswers[path] = dirSize
    if path == '/':
        hdSize = dirSize


solution = 10000000000
for answer in possibleAnswers:
    currentItem = possibleAnswers[answer]
    if currentItem < solution:
        solution = currentItem

print('the solution is: ', solution)
