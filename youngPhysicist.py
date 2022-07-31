forces_num = eval(input())
vector = []
totalForce = [0, 0, 0]

for i in range(forces_num):
    force = input()
    forces = force.split(" ")
    vector.append(forces)

for row_index in range(len(vector)):
    for column_index in range(len(vector[row_index])):
        column_value = int(vector[row_index][column_index])
        totalForce[column_index] = totalForce[column_index] + column_value

if totalForce[0] == 0 and totalForce[1] == 0 and totalForce[2] == 0:
    print("YES")
else:
    print("NO")
