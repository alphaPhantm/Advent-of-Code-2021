from collections import Counter, OrderedDict
from itertools import islice, cycle


def shift_dict(dct, shift):
    shift %= len(dct)
    return OrderedDict((k, v) for k, v in zip(dct.keys(), islice(cycle(dct.values()), shift, None)))


with open("6data.txt") as f:
    initial_state = f.read().split(",")

for z in range(len(initial_state)):
    initial_state[z] = int(initial_state[z])

mapNormal = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
mapNew = {7: 0, 8: 0}

for i in range(len(initial_state)):
    mapNormal[int(initial_state[i])] += 1

for d in range(256):
    new_fishes = mapNormal[0]
    mapNormal = shift_dict(mapNormal, 1)
    mapNormal[6] += mapNew[7]
    mapNew[7] = mapNew[8]
    mapNew[8] = new_fishes

x = sum(mapNormal.values()) + sum(mapNew.values())
print(x)