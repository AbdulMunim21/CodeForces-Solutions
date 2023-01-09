import math
t = eval(input())
output_list = []

for _ in range(t):
    length = eval(input())
    setValues = input()
    setValues = setValues.split(" ")
    setValues = [int(x) for x in setValues]
    output_list.append(int(setValues[-1]/math.gcd(*setValues)))


for i in output_list:
    print(i)