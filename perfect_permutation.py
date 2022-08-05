test_cases = input()
weights = []
for test in range(int(test_cases)):
    weights.append(input())


for weight in weights:
    weight = int(weight)
    if weight == 1:
        print(1)
    else:
        print(weight, end=" ")
        for i in range(weight-1):
            print(i+1, end=" ")
