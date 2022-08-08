value = input()
value = value.split(" ")
value = [int(i) for i in value]
times = value[1]
arrangement = input()
arrangement = list(arrangement)
index = 0
while times > 0:
    while index < len(arrangement)-1:
        if arrangement[index] == "B" and arrangement[index+1] == "G":
            temp = arrangement[index]
            arrangement[index] = arrangement[index+1]
            arrangement[index+1] = temp
            index += 1
        else:
            index += 1
        index += 1
    index = 0
    times -= 1


for val in arrangement:
    print(val, end="")
