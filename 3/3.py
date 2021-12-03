with open("3data.txt") as f:
    lines = f.read().splitlines()

for i in range(len(lines)):
    lines[i] = list(lines[i])

for x in range(len(lines)):
    for y in range(len([lines[x]])):
        lines[x][y] = int(lines[x][y])

gamma = []
epsilon = []

count0 = 0
count1 = 0

for x in range(len(lines[x])):
    for y in range(len(lines)):
        if lines[y][x] == 0:
            count0 += 1
        else:
            count1 += 1

    if count1 > count0:
        gamma.append(1)
        epsilon.append(0)
    elif count1 < count0:
        gamma.append(0)
        epsilon.append(1)

gs = [str(integer) for integer in gamma]
ags = "".join(gs)
g = int(ags)

es = [str(integer) for integer in epsilon]
aes = "".join(es)
e = int(aes)


print(g)
print(e)



