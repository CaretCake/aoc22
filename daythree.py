def get_priority(item):
    subtractValue = 38
    if item.islower():
        subtractValue = 96
    return (ord(item) - subtractValue)


file = open("input.txt", "r")


items = []
result = 0

for line in file:
    rucksackItems = ' '.join(line.split())
    firstCompartment, secondCompartment = rucksackItems[:len(rucksackItems)//2], rucksackItems[len(rucksackItems)//2:]
    items = items + list((set(firstCompartment).intersection(secondCompartment)))

for item in items:
    result += get_priority(item)

print(result)

file.close()