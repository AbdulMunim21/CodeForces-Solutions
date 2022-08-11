values = input()
values = values.split(" ")
numItems = int(values[0])
queries = int(values[1])

prices = input()
prices = prices.split(" ")
pricesArr = [int(x) for x in prices]
pricesArr.sort(reverse=True)

while queries > 0:
    values = input()
    values = values.split(" ")
    x = int(values[0])
    y = int(values[1])
    purchasedArr = []
    for i in range(x):
        purchasedArr.append(pricesArr[i])

    lastValues = purchasedArr[y-1:x]
    sum = 0
    for i in lastValues:
        sum += i

    print(sum)

    queries -= 1
