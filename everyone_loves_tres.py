input_num = int(input())
results_list = []

while(input_num > 0):
    input_num -=1
    decimal_count = input()
    int_decimal_count = int(decimal_count)
    inner_result = []
    starting_num = "1" + ("0" * (int_decimal_count - 1))
    ending_num_in_str = "9" + ("9" * (int_decimal_count - 1))
    threes = int(("3" * int_decimal_count))
    sixes = int(("6" * int_decimal_count))
    int_starting_num = int(starting_num)
    
    while(int_starting_num <= int(ending_num_in_str)):
        if int_starting_num % threes == 0 and int_starting_num % sixes == 0:
            inner_result.append(int_starting_num)
        int_starting_num = int_starting_num + 1
    
    inner_result.sort()
    if len(inner_result) == 0:
        results_list.insert(len(results_list), -1)
    else:
        results_list.insert(len(results_list), inner_result[0])
        
for i in results_list:
    print(i)
        
        
#? Work in Progress - https://codeforces.com/problemset/problem/2035/B