def check_win(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            try:
                if grid[y][x] == 222 and grid[y][x + 1] == 222 and grid[y][x + 2] == 222 and grid[y][x + 3] == 222 and \
                        grid[y][x + 4] == 222:
                    return True
                if grid[y][x] == 222 and grid[y + 1][x] == 222 and grid[y + 2][x] == 222 and grid[y + 3][x] == 222 and \
                        grid[y + 4][x] == 222:
                    return True
            except IndexError:
                next


with open("4data.txt") as f:
    lines = f.read().splitlines()


def sum(grid):
    sum = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] != 222:
                sum += grid[x][y]
    return sum


def has_won(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] = 222
    return grid


grid = []
grids = []
count = 0

for i in range(len(lines)):
    lines[i] = (lines[i].split(" "))
    x = []
    for t in range(len(lines[i])):
        if lines[i][t] == "":
            pass
        else:
            x.append(int(lines[i][t]))
    if x != []:
        grid.append(x)
        count += 1

    if count == 5:
        grids.append(grid)
        grid = []
        count = 0

with open("4dataCalls.txt") as f:
    calls = f.read().split(",")

for i in range(len(calls)):
    calls[i] = int(calls[i])

print("")

wonn_grids = []
score = []

for call in range(len(calls)):
    for gird in range(len(grids)):
        for line in range(len(grids[gird])):
            for num in range(len(grids[gird][line])):
                if grids[gird][line][num] == calls[call]:
                    grids[gird][line][num] = 222
        if check_win(grids[gird]):
            if calls[call] * sum(grids[gird]) > 0:
                score.append(calls[call] * sum(grids[gird]))
                grids[gird] = [[222, 222, 222, 222, 222], [222, 222, 222, 222, 222], [222, 222, 222, 222, 222], [222, 222, 222, 222, 222], [222, 222, 222, 222, 222]]
print(score)

# 3 Score Values to much.