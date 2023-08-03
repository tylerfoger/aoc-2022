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


def visibleTrees(trees, map):
    totalVisibleTrees = 0

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

        if biggerTree(treeHeight, tallestLeft):
            visible = True
        elif biggerTree(treeHeight, tallestRight):
            visible = True
        elif biggerTree(treeHeight, tallestUp):
            visible = True
        elif biggerTree(treeHeight, tallestDown):
            visible = True
        if visible:
            totalVisibleTrees += 1
        else:
            pass

    return totalVisibleTrees


def getTallestTree(treeRange):
    if treeRange != []:
        tallestTree = int(reduce(lambda a, b: a if a > b else b, treeRange))
    else:
        tallestTree = -1
    return tallestTree


def biggerTree(a, b):
    if a > b:
        return True
    else:
        return False

map = generateMap()
trees = treeInfo(map)

answer = visibleTrees(trees, map)
print('the answer is: ', answer)
