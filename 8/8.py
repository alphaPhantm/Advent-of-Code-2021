import numpy as np

def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key

with open("8data.in") as d:
    raw_data = d.read().strip().split("\n")

input_data = [[line[:line.index("|") - 1].split(" "), line[line.index("|") + 2:].split(" ")] for line in raw_data]

erg = []

for i in range(len(input_data)):
    map = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
    }

    remove = []

    for y in range(len(input_data[i][0])):
        if len(input_data[i][0][y]) == 2:
            map[1] = input_data[i][0][y]

        elif len(input_data[i][0][y]) == 3:
            map[7] = input_data[i][0][y]

        elif len(input_data[i][0][y]) == 4:
            map[4] = input_data[i][0][y]

        elif len(input_data[i][0][y]) == 7:
            map[8] = input_data[i][0][y]

    for y in range(len(input_data[i][0])):
        if len(input_data[i][0][y]) == 5:
            if map[1][0] in input_data[i][0][y] and map[1][1] in input_data[i][0][y]:
                map[3] = input_data[i][0][y]
            else:
                x = list(set(map[4]) - set(map[1]))
                if x[0] in input_data[i][0][y] and x[1] in input_data[i][0][y]:
                    map[5] = input_data[i][0][y]
                else:
                    map[2] = input_data[i][0][y]

        elif len(input_data[i][0][y]) == 6:
            if map[1][0] in input_data[i][0][y] and map[1][1] in input_data[i][0][y]:
                if map[4][0] in input_data[i][0][y] and map[4][1] in input_data[i][0][y] and map[4][2] in \
                        input_data[i][0][y] and map[4][3] in input_data[i][0][y]:
                    map[9] = input_data[i][0][y]
                else:
                    map[0] = input_data[i][0][y]
            else:
                map[6] = input_data[i][0][y]

    for m in range(len(map)):
        map[m] = sum([ord(c) for c in map[m]])

    s = []
    for e in range(len(input_data[i][1])):
        s.append(get_key(map, sum([ord(c) for c in input_data[i][1][e]])))

    erg.append(int("".join([str(integer) for integer in s])))

print(sum(erg))