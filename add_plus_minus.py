test_cases = eval(input())
queue = []
output_list = []
currentTest = 0


while currentTest < test_cases :
    length = eval(input())
    string = input()

    output_list.append("")

    queue.append(int(string[0]))

    for i in range(1,len(string)):
        element = queue.pop()
        queueElement = int(string[i])
        if (element == 0 and queueElement == 1) or (element == 1 and queueElement == 0) or (element == 0 and queueElement == 0):
            newVal = element + queueElement
            queue.append(newVal)
            output_list[currentTest] += "+"
        else:
            newVal = element - queueElement
            queue.append(newVal)
            output_list[currentTest] += "-"

    currentTest+=1
    queue = []

for i in output_list:
    print(i)
# print(queue)
