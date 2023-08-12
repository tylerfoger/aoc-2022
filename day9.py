

def moveHead(headPath):
    gridX = [[0]]
    gridY = [[0]]
    headX = 0
    headY = 0
    tailX = 0

    for path in headPath:
        direction = path[0]
        distance = int(path[1])

        print(direction, distance)
        if direction in ['L', 'D']:
            distance *= -1
        if direction == 'L':
            pass
        elif direction == 'R':
            pass
        elif direction == 'U':
            pass
        elif direction == 'D':
            pass
        if direction in ['L', 'R']:
            print(distance, headX, len(gridX))
            headX += distance
            print(distance, headX, len(gridX))
            if headX > len(gridX):
                print('farther horizontally')
                newX = updateValues(len(gridX) - distance, gridX)
                gridX = newX
            elif headX < 0:
                # to the left of 0
                print(f'add {distance * -1} rows to the left')
                pass
            else:
                print('within horizontal boundary')
            headX += distance
        elif direction in ['U', 'D']:
            print(distance, headY, len(gridY))
            if (distance + headY) > len(gridY):
                print('farther vertically')
                print(direction, distance)
                newY = updateValues(distance - len(gridY), gridY)
                gridY = newY
            elif (distance + headY) < 0:
                # below 0
                pass
            else:
                print('within vertical boundary')
            headY += distance
        else:
            print(direction, "this shouldn't happen")

    return gridX


def updateValues(value, axis):
    print(value)
    if value < 0:
        print('negative number')
        itemsToAdd = [0] * (value * -1)
        print(itemsToAdd)
        newList = itemsToAdd + axis
    else:
        itemsToAdd = [0] * value
        newList = axis + itemsToAdd
        # set all other rows to same width, all 0
        # create new row with length of the current width, all 0

    return newList

def getHeadPath():
    pathList = []
    with open('day9-input.txt', 'r') as input:
        for line in input.readlines():
            pathList.append(line.split())
    return pathList


def newRow():
    pass


def newColumn():
    pass




headPath = getHeadPath()
print(moveHead(headPath))
