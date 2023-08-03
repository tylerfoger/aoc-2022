from functools import reduce


def generateMap():
    rowIter = 1
    columns = []
    rows = []

    with open('day8-input.txt', 'r') as input:
        for line in input.readlines():
            newRow = []
            for item in line:
                if item == '\n':
                    pass
                else:
                    newRow.append(int(item))
            rows.append(newRow)
            rowIter += 1
            for i, column in enumerate(line):
                if i == '\n':
                    pass
                elif i <= 98:
                    try:
                        columns[i].append(newRow[i])
                    except IndexError:
                        columns.append([])
                        columns[i].append(newRow[i])
    return {'rows': rows, 'columns': columns}


def treeInfo(map):
    rows = map['rows']
    trees = {}
    currentTree = 0

    for rowIndex, row in enumerate(rows):
        for i, tree in enumerate(row):
            trees[currentTree] = {
                    'height': tree,
                    'x': rowIndex,
                    'y': i
            }
            currentTree += 1

    return trees


def evaluateTrees(trees, map):
    totalVisibleTrees = 0
    biggestScore = 0

    for tree in trees:
        visible = False
        currentTree = trees[tree]
        treeHeight = currentTree['height']
        treeXPos = currentTree['x']
        treeYPos = currentTree['y']
        currentRow = map['rows'][treeXPos]
        currentCol = map['columns'][treeYPos]
        treesLeft = currentRow[0:(treeYPos)]
        treesRight = currentRow[(treeYPos + 1):]
        treesUp = currentCol[0:(treeXPos)]
        treesDown = currentCol[(treeXPos + 1):]
        tallestLeft = getTallestTree(treesLeft)
        tallestRight = getTallestTree(treesRight)
        tallestUp = getTallestTree(treesUp)
        tallestDown = getTallestTree(treesDown)
        scoreLeft = getTreeScore(currentTree['height'], treesLeft[::-1])
        scoreRight = getTreeScore(currentTree['height'], treesRight)
        scoreUp = getTreeScore(currentTree['height'], treesUp[::-1])
        scoreDown = getTreeScore(currentTree['height'], treesDown)

        treeScore = scoreLeft * scoreRight * scoreUp * scoreDown
        if biggerTree(treeHeight, tallestLeft):
            visible = True
        if biggerTree(treeHeight, tallestRight):
            visible = True
        if biggerTree(treeHeight, tallestUp):
            visible = True
        if biggerTree(treeHeight, tallestDown):
            visible = True
        if visible:
            totalVisibleTrees += 1
        if treeScore > biggestScore:
            biggestScore = treeScore

    return totalVisibleTrees, biggestScore


def getTallestTree(treeRange):
    if treeRange != []:
        tallestTree = int(reduce(lambda a, b: a if a > b else b, treeRange))
    else:
        return -1

    return tallestTree


def getTreeScore(currentTree, treeList):
    if treeList not in [None, []]:
        for index, value in enumerate(treeList):
            if value >= currentTree:
                if index == 0:
                    return 1
                return index + 1
        return len(treeList)
    else:
        treeScore = 0

    return treeScore


def biggerTree(a, b):
    if a > b:
        return True
    else:
        return False


def find_first_larger_element_index(input_list, target):
    print(target, input_list)
    for index, value in enumerate(input_list):
        if value > target:
            print('larger, score is: ', index)
            if index == 0:
                return 1
            return index
    return len(input_list)


map = generateMap()
trees = treeInfo(map)
answer = evaluateTrees(trees, map)
print('the answer is: ', answer)
