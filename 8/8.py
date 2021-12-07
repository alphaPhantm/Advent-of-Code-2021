def Average(lst):
    return sum(lst) / len(lst)


with open("8data.txt") as f:
    initial_state = f.read().split(",")

for z in range(len(initial_state)):
    initial_state[z] = int(initial_state[z])


maxN = max(initial_state)
minN = min(initial_state)
count = []
c = 0
lst = initial_state.copy()
print(len(initial_state))
print(minN)
print(maxN)

# avg = round(Average(initial_state))
# print(avg)
#
# for i in range(len(initial_state)):
#     z = 1
#     while initial_state[i] > avg:
#         c += z
#         z += 1
#         initial_state[i] -= 1
#     while initial_state[i] < avg:
#         c += z
#         z += 1
#         initial_state[i] += 1
#
#
# print(c)

for x in range(minN, maxN):
    for i in range(len(lst)):
        z = 1
        while lst[i] < x:
            c += z
            z += 1
            lst[i] += 1
        while lst[i] > x:
            c += z
            z += 1
            lst[i] -= 1

    count.append(c)
    c = 0
    lst = initial_state.copy()
    print(x)




print(min(count))