
coins = eval(input())
coins_array = []
sum = 0
minimumcoins = 0
sum_minimum = 0
value = input()
value = value.split(" ")
for val in value:
    coins_array.append(int(val))
    sum += int(val)
coins_array.sort()
for i in range(coins-1, -1, -1):
    sum_minimum += coins_array[i]
    if sum_minimum > (sum - sum_minimum):
        minimumcoins += 1
        break
    minimumcoins += 1

print(minimumcoins)
