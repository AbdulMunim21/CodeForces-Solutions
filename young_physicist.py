lines = eval(input())
twoDArr = []
answers = [0, 0, 0]
for i in range(lines):
    value = input()
    seperated = value.split(" ")
    twoDArr.append([int(seperated[0]), int(seperated[1]), int(seperated[2])])
for i in range(lines):

    for j in range(len(twoDArr[i])):
        answers[j] += twoDArr[i][j]

condition = True
for i in answers:
    if i != 0:
        condition = True
        break
    else:
        condition = False

if condition:
    print("NO")
else:
    print("YES")
