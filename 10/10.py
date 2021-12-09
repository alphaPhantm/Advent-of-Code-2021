import numpy
import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open("10data.in") as d:
    raw_data = d.read().split()
    input_data = [[int(num) for num in list(line)] for line in raw_data]

xoff = [1, 0, -1, 0]
yoff = [0, 1, 0, -1]
deep_points = []
count = 0

for y in range(len(input_data)):
    for x in range(len(input_data[y])):
        has_lower = False
        for i in range(4):
            if not (y + yoff[i] < 0 or x + xoff[i] < 0 or y + yoff[i] > len(input_data) - 1 or x + xoff[i] > len(
                    input_data[y]) - 1):
                if input_data[y + yoff[i]][x + xoff[i]] <= input_data[y][x]:
                    has_lower = True
                    break
        if not has_lower:
            deep_points.append([x, y, 0])

for y in range(len(input_data)):
    for x in range(len(input_data[y])):
        if input_data[y][x] == 9:
            input_data[y][x] = 0
        else:
            input_data[y][x] = 1


grid = Grid(matrix=input_data)
for i in range(len(deep_points)):
    start = grid.node(deep_points[i][0], deep_points[i][1])
    end = grid.node(9, 4)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    _, deep_points[i][2] = finder.find_path(start, end, grid)

res = []
for i in range(len(deep_points)):
    res.append(deep_points[i][2])

arr = np.array(res)
ind = arr.argsort()[-3:][::-1]

a_list = arr[ind]
multiplied_list = numpy.prod(a_list)
print(multiplied_list)

