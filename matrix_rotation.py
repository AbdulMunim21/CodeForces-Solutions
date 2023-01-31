## matrix [[1,3],[5,7]]


def rotate(matrix):
    for row in range(len(matrix)):
        temp = matrix[row][1]
        matrix[row][1] = matrix[row][0]
        matrix[row][0] = temp
    temp = matrix[0][0]
    matrix[0][0] = matrix[1][1]
    matrix[1][1] = temp
    return matrix

def checkConditions(matrix):
    for rowIndex in range(len(matrix)):
        if matrix[rowIndex][0] >= matrix[rowIndex][1]:
            # print('oops row', matrix[rowIndex][0], matrix[rowIndex][1])
            return False

    for columnIndex in range(len(matrix[0])):
        if matrix[0][columnIndex] >= matrix[1][columnIndex]:
            # print('oops column')
            return False
    return True

outputArr = []
test_cases = eval(input())
for _ in range(0,test_cases):
    firstLine = input()
    secondLine = input()
    firstRow = [int(firstLine.split(" ")[0]),int(firstLine.split(" ")[1])]
    secondRow = [int(secondLine.split(" ")[0]),int(secondLine.split(" ")[1])]
    matrix = [firstRow, secondRow]
    # print("Matrix", matrix)
    
    for _ in range(0,4):
        condition = checkConditions(matrix)
        # print("New Matrix", matrix, "Condition",condition)
        if condition:
            outputArr.append("YES")
            break
        else:
            matrix = rotate(matrix)
    condition = checkConditions(matrix)
    if condition == False:
        outputArr.append("NO")


for i in outputArr:
    print(i)


