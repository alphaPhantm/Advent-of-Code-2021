with open("3data.txt") as f:
    lines = f.read().splitlines()

for i in range(len(lines)):
    lines[i] = list(lines[i])

for y in range(len(lines)):
    for x in range(len(lines[y])):
        lines[y][x] = int(lines[y][x])

generator = 0
scrubber = 0

for x in range(12):

    count0 = 0
    count1 = 0

    for y in range(len(lines)):
        if lines[y][x] == 0:
            count0 += 1
        elif lines[y][x] == 1:
            count1 += 1

    if count1 >= count0:
        generator = 1
        scrubber = 0
    elif count1 < count0:
        generator = 0
        scrubber = 1

    for line in lines:
        if line[x] != generator:
            lines.remove(line)



print(lines)
