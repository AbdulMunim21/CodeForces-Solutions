number = input()

luckyNumberCount = 0
luckyNumber = True
for val in range(len(number)):
    if number[val] != "7" or number[val] != "4":
        luckyNumber = False
        break

if luckyNumber is False:
    for val in range(len(number)):
        if number[val] == "7" or number[val] == "4":
            luckyNumberCount += 1

if luckyNumberCount == 7 or luckyNumberCount == 4:
    luckyNumber = True
print("YES" if luckyNumber is True else "NO")
