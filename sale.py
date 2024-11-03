ask = input().split(" ")
num_of_tv = int(ask[0])
num_of_tv_carried = int(ask[1])

tv_list = [int(x) for x in input().split(" ")]
tv_list = sorted(tv_list)

money=0
for i in tv_list[0:num_of_tv_carried]:
    if i < 0:
        money+=i
    
print(abs(money))
