def file_2_list(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    for i in range(len(lines)):
        lines[i] = int(lines[i])

    return lines

if __name__ == '__main__':

    data = file_2_list("1data.txt")

    count = 0

    list = []

    for i in range(len(data)-2):
        list.append(data[i] + data[i+1] + data[i+2])

    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            count+=1

    print(count)