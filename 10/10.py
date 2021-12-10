with open("10data.in") as d:
    input_data = d.read().splitlines()

openList = ["[", "{", "(", "<"]
closeList = ["]", "}", ")", ">"]


def balance(myStr):
    stack = []
    for i in myStr:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if (len(stack) > 0) and (openList[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return True, i
    if len(stack) == 0:
        return True, 0
    else:
        return False, stack



score = []
for line in input_data:
    balanced, bracket = balance(line)
    if not balanced:
        count = 0
        for i in range(len(bracket) - 1, -1 , -1):
            count *= 5
            if bracket[i] == "(":
                count += 1
            elif bracket[i] == "[":
                count += 2
            elif bracket[i] == "{":
                count += 3
            elif bracket[i] == "<":
                count += 4

        score.append(count)

score.sort()
print(len(score))
print(score[int(len(score) / 2)])
