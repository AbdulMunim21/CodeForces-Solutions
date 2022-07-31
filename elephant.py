position = eval(input())
condition = True
steps = 0
while condition:
    if position >= 5:
        steps += 1
        position = position - 5
    elif position >= 4:
        steps += 1
        position = position - 4

    elif position >= 3:
        steps += 1
        position = position - 3

    elif position >= 2:
        steps += 1
        position = position - 2

    elif position >= 1:
        steps += 1
        position = position - 1

    if position == 0:
        condition = False

print(steps)
