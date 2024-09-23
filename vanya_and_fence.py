first_input = input().split(" ")
friends = int(first_input[0])
height = int(first_input[1])

second_input = input().split(" ")

width = 0

for i in second_input:
    if int(i) > height: 
        width += 2
    else:
        width += 1

print(width)
