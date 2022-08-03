num1 = eval(input())
num2 = eval(input())
num3 = eval(input())

answer = num1 + num2 + num3

answer = max(answer, num1 * num2 + num3)
answer = max(answer, num1 * num2 * num3)
answer = max(answer, (num1 + num2) * num3)
answer = max(answer, num1 + (num2 * num3))
answer = max(answer, num1 * (num2 + num3))

print(answer)
