with open("8data.in") as d:
    raw_data = d.read().strip().split("\n")

input_data = [[line[:line.index("|") - 1].split(" "), line[line.index("|") + 2:].split(" ")] for line in raw_data]


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
    for y in range(len(input_data[i][0])):
        if len(input_data[i][0][y]) == 2:
            map[1] = input_data[i][0][y]
        elif len(input_data[i][0][y]) == 3:
            map[7] = input_data[i][0][y]
        elif len(input_data[i][0][y]) == 4:
            map[7] = input_data[i][0][y]
        elif len(input_data[i][0][y]) == 7:
            map[8] = input_data[i][0][y]



