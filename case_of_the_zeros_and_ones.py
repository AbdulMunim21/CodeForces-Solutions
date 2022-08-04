length = eval(input())
new_length = []
string = input()
zeros_values = 0
ones_values = 0

for i in string:
    new_length.append(int(i))

new_length.sort()

for i in new_length:
    if i == 0:
        zeros_values += 1
    else:
        ones_values += 1

total = abs(zeros_values - ones_values)

print(total)
