test_cases = eval(input())
answers = []

for i in range(test_cases):
    length = eval(input())
    string = input()
    string = string.split(" ")
    string = [int(x) for x in string]
    steps = 0
    changeNum = 0
    holdNum = 0
    # print("original String: " + str(string))
    for j in range(len(string) + 1):
        for k in range(changeNum+1, len(string)):
            if string[changeNum] == string[k]:
                steps += 1
                string.pop(0)
                break
            else:
                holdNum = string[0]

        if holdNum == string[0]:
            changeNum += 1
            holdNum = 0

        print(string)
    answers.append(steps)
    steps = 0
    changeNum = 0

for val in answers:
    print(val)
