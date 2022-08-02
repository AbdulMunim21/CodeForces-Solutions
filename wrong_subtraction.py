string = input()

seperated = string.split(" ")
value = int(seperated[0])
times = int(seperated[1])

for i in range(times):
    if str(value)[-1] == "0":
        value = int(value / 10)
    else:
        value = value - 1


print(value)
