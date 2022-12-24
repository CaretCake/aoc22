import time
def main():
    file = open("input.txt", "r")
    stacks = build_stacks(file)
    for line in file:
        if not line.isspace():
            moveValues = get_move_values(line)
            numOfItems = moveValues[0]
            sourceStack = moveValues[1]
            destinationStack = moveValues[2]
            
            itemsToMove = stacks[sourceStack][-numOfItems:]
            stacks[sourceStack] = stacks[sourceStack][:len(stacks[sourceStack])-numOfItems]
            stacks[destinationStack].extend(itemsToMove)
    topItems = ''
    for stack in stacks:
        topItems += stack.pop()
    print(topItems)
    file.close()


#Input:
#    [#]
#[#] [#]
#[#] [#] [#]
# 1   2   3

# Returns list with [0]:# to move, [1]:source stack, [2]]:destination stack
def get_move_values(line):
    splitLine = line.rstrip('\n').split(' ')
    return [
        int(splitLine[1]),
        int(splitLine[3])-1,
        int(splitLine[5])-1
    ]

def separate_items(itemList):
    items = []
    chunks = [itemList[i:i+4] for i in range(0, len(itemList), 4)]
    for chunk in chunks:
        items.append(chunk[1])
    return items

def is_valid_item(item):
    return not item.isspace() and len(item) > 0

def build_stacks(file):
    itemLists = []
    stackCount = 0
    for line in file:
        items = line.rstrip('\n')
        if stackCount == 0:
            stackCount = int((len(items) + 1) / 4)
        if items.startswith(' 1'):
            break
        itemLists.append(separate_items(items))
    itemLists.reverse()
    builtStacks = [[] for i in range(0, stackCount)]
    for itemList in itemLists:
        for stackIndex in range(stackCount):
            item = itemList[stackIndex]
            if is_valid_item(item):
                builtStacks[stackIndex].append(item)
    return builtStacks

if __name__ == '__main__':
    main()
