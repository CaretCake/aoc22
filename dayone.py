file = open("input.txt", "r")


maxCalories = [0,0,0]
calories = 0

for line in file:
    if line == '\n':
        if maxCalories[0] < calories:
            maxCalories[0] = calories
            maxCalories.sort()
        calories = 0
    else:
        calories += int(line)

print(sum(maxCalories))

file.close()