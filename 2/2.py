with open("2data.txt") as f:
    lines = f.read().splitlines()

direction = []
lenght = []

for i in range(len(lines)):
    direction.append(lines[i].split(" ")[0])
    lenght.append(int(lines[i].split(" ")[1]))

depth = 0
x = 0
aim = 0

for i in range(len(direction)):
    if direction[i] == "forward":
        x = x + lenght[i]
        depth = depth + (aim * lenght[i])
    elif direction[i] == "down":
        aim = aim + lenght[i]
    elif direction[i] == "up":
        aim = aim - lenght[i]

print(depth * x)
