def newElf(id, calories):
    return {
            'id': id,
            'calories': calories,
            'calorieSum': sumCalories(calories)
    }


def sumCalories(calories):
    total = 0

    for ele in range(0, len(calories)):
        total = total + calories[ele]

    return total


def createElves():
    array = []
    currentElf = 0
    allElves = []

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            if line == '\n':
                currentElf += 1
                nextElf = newElf(currentElf, array)
                allElves.append(nextElf)
                del array[:]
            else:
                array.append(int(line))
    return allElves


def top3Fat(elves):
    allElves = []

    for elf in elves:
        calories = elf['calorieSum']
        allElves.append(calories)

    allElves.sort(reverse=True)
    top3 = allElves[0] + allElves[1] + allElves[2]

    return top3


def fattestElf(elves):
    highCal = 0
    fatElf = 0
    for elf in elves:
        calories = elf['calorieSum']
        if calories > highCal:
            highCal = calories
            fatElf = elf['id']

    return fatElf, highCal


elves = createElves()
fatElf = fattestElf(elves)
top3 = top3Fat(elves)
print(top3)
