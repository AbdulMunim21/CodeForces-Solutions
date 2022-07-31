position = eval(input())
condition = True
steps = 0
while condition:
    if position % 5 == 0:
        steps += 1
        position = position - 5
    elif position % 4 == 0:
        steps += 1
        position = position - 4

    elif position % 3 == 0:
        steps += 1
        position = position - 3

    elif position % 2 == 0:
        steps += 1
        position = position - 2

    elif position % 1 == 0:
        steps += 1
        position = position - 1

    if position == 0:
        condition = False

print(steps)
