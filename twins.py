# int coins = x.nextInt()
# int[] coins_array = new int[coins]
# long sum = 0
# int minimumcoins = 0
# int sum_minimum = 0
# for (int i=0
#      i < coins
#      i++)
# {
#     int value = x.nextInt()
#     coins_array[i] = value
#     sum += value
# }
# Arrays.sort(coins_array)
# for(int i=coins-1
#     i >= 0
#     i--)
# {
#     sum_minimum += coins_array[i]
#     if(sum_minimum > (sum - sum_minimum))
#     {
#         minimumcoins++
#         break
#     }
#     minimumcoins++
# }
# System.out.println(minimumcoins)


# coins = eval(input())
# coins_array = []
# sum = 0
# minimumcoins = 0
# sum_minimum = 0
# value = input()
# value = value.replace(" ", '')
# value = int(value)
# coins_array.append(value)
# sum += value
# coins_array.sort()
# for i in range(coins-1, -1, -1):
#     sum_minimum += coins_array[i]
#     if sum_minimum > (sum - sum_minimum):
#         minimumcoins += 1
#         break
#     minimumcoins += 1

# print(minimumcoins)
