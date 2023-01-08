test_case = eval(input())
output_list = []

for i in range(test_case):
    a_b = input()
    value = a_b.split("+")
    a = int(value[0])
    b = int(value[1])

    output_list.append(a+b)

for i in output_list:
    print(i)
    