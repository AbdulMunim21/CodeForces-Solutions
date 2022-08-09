test_cases = eval(input())
answer = ""
while test_cases:
    answer = ""
    value = eval(input())
    for i in range(9, 0, -1):
        if value >= i:
            answer = str(i) + answer
            value -= i

        if value == 0:
            break

    test_cases -= 1
    print(answer)

