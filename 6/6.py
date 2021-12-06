with open("6data.txt") as f:
    initial_state = f.read().split(",")

for z in range(len(initial_state)):
    initial_state[z] = int(initial_state[z])

for d in range(256):
    for i in range(len(initial_state)):
        if initial_state[i] == 0:
            initial_state[i] = 6
            initial_state.append(8)
        else:
            initial_state[i] -= 1
    print(d)

print(len(initial_state))