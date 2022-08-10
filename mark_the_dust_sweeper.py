test_cases = eval(input())
num_index = 0
answer = 0

while test_cases:
    num_rooms = eval(input())
    dust_levels = input()
    dust_levels = dust_levels.split(" ")
    dust_levels = [int(x) for x in dust_levels]
    while(dust_levels[num_index] == 0 and num_index < num_rooms):
        num_index += 1
    for i in range(num_index, num_rooms-1, 1):
        answer += dust_levels[i]
        if dust_levels[i] == 0:
            answer += 1
            
    print(answer)

    answer = 0
    num_index = 0
    test_cases -= 1