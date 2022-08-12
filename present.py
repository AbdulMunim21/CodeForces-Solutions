numFriends = eval(input())
friends = input()
friends = friends.split(" ")
answer = []
obj = {}
for i in range(numFriends):
    obj[i+1] = int(friends[i])
    answer.append(0)

for key, value in obj.items():
    answer[value-1] = key


for val in answer:
    print(val, end=" ")
