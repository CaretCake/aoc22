def get_priority(item):
    subtractValue = 38
    if item.islower():
        subtractValue = 96
    return (ord(item) - subtractValue)


file = open("input.txt", "r")

packs = []
badges = []
result = 0

for line in file:
    rucksackItems = ' '.join(line.split())
    if (len(packs) == 3):
        packs = []
    packs.append(rucksackItems)
    if (len(packs) < 3): continue
    badges = badges + list((set(packs[0]).intersection(packs[1]).intersection(packs[2])))

for badge in badges:
    result += get_priority(badge)

print(result)

file.close()