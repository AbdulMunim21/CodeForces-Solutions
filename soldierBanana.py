inputs = input()
seperated = inputs.split(" ")

banana_cost = int(seperated[0])
soldier_cost = int(seperated[1])
banana_wants = int(seperated[2])
total_cost = 0

for i in range(banana_wants):
    total_cost = total_cost + (banana_cost * (i+1))

total_cost = total_cost - soldier_cost

print(total_cost)
