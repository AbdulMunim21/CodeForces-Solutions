test_cases = eval(input())
answers = []
steps = 0

while test_cases > 0:
    values = input()
    seperated = values.split(" ")
    rows = int(seperated[0])
    columns = int(seperated[1])
    steps = (columns*(columns+1))/2
    tempM = columns
    for i in range(2, rows+1):
        tempM += columns
        steps += int(tempM)
    print(int(steps))
    test_cases -= 1
