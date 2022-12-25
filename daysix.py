import time
def main():
    print_marker(4)
    print_marker(14)



def print_marker(markerLength):
    file = open("input.txt", "r")
    left = 0
    right = 1
    for line in file:
        while right < len(line):
            if right < markerLength:
                right += 1
                continue
            potentialMarker = line[left:right]
            markerSet = set(potentialMarker)
            if len(markerSet) == markerLength:
                print(f"{potentialMarker} : {right}")
                break
            left += 1
            right += 1
    file.close()

if __name__ == '__main__':
    main()