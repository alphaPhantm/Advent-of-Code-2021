with open("6data.txt") as f:
    lines = f.read().splitlines()

# [x, y]
start = []
end = []

maxX = 0
maxY = 0

for line in lines:
    start.append([int(i) for i in line.split("->")[0].split(",")])
    end.append([int(i) for i in line.split("->")[1].split(",")])

for i in range(len(lines)):
    if start[i][0] > maxX:
        maxX = start[i][0]
    if end[i][0] > maxX:
        maxX = end[i][0]
    if start[i][1] > maxY:
        maxY = start[i][1]
    if end[i][1] > maxY:
        maxY = end[i][1]

map = []

for i in range(maxY + 1):
    map.append([])
    for j in range(maxX + 1):
        map[i].append(0)

for line in range(len(lines)):
    if start[line][0] == end[line][0]:
        if end[line][1] > start[line][1]:
            for y in range(start[line][1], end[line][1] + 1):
                map[y][start[line][0]] += 1
        else:
            for y in range(end[line][1], start[line][1] + 1):
                map[y][start[line][0]] += 1
    elif start[line][1] == end[line][1]:
        if end[line][0] > start[line][0]:
            for x in range(start[line][0], end[line][0] + 1):
                map[start[line][1]][x] += 1
        else:
            for x in range(end[line][0], start[line][0] + 1):
                map[start[line][1]][x] += 1
    else:
        if end[line][1] > start[line][1]:
            if end[line][0] > start[line][0]:
                x = start[line][0]
                for y in range(start[line][1], end[line][1] + 1):
                    map[y][x] += 1
                    x += 1
            else:
                x = start[line][0]
                for y in range(start[line][1], end[line][1] + 1):
                    map[y][x] += 1
                    x -= 1
        else:
            if end[line][0] > start[line][0]:
                x = end[line][0]
                for y in range(end[line][1], start[line][1] + 1):
                    map[y][x] += 1
                    x -= 1
            else:
                x = end[line][0]
                for y in range(end[line][1], start[line][1] + 1):
                    map[y][x] += 1
                    x += 1

count = 0


for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] >= 2:
            count += 1


print(count)
