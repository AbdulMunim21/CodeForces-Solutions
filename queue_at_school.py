value = input()
value = value.split(" ")
value = [int(i) for i in value]
times = value[1]
arrangement = input()
arrangement = list(arrangement)
dummy_arr = arrangement[:]

for i in range(0,times):
    for j in range(0,len(arrangement)-1):
        if arrangement[j] == "B" and arrangement[j+1] == "G":
            temp = dummy_arr[j]
            dummy_arr[j] = dummy_arr[j+1]
            dummy_arr[j+1] = temp
    
    arrangement = dummy_arr[:]


for val in arrangement:
    print(val, end="")
