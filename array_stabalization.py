length = eval(input())

values = input()
values = values.split(" ")
values = [int(x) for x in values]

values = sorted(values)


print(min(values[length - 2] - values[0], values[length - 1] - values[1]))