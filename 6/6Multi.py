from collections import Counter

with open("6data.txt") as f:
    initial_state = f.read().split(",")

for z in range(len(initial_state)):
    initial_state[z] = int(initial_state[z])

new = Counter(initial_state)
print(new)
for j in range(256):
    temp = Counter()
    for p in new:
        if p -1 == p:
            temp[6] += new[p]
            temp[8] += new[p]
        else:
            temp[p-1] += new[p]
    print(temp)
    new = temp.copy()

ans(sum(new.values()))