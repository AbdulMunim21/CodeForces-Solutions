result = []
input_count = int(input())
def has_odd_divisor(n):
    # If n is 1, it doesn't have an odd divisor greater than 1
    if n == 1:
        return False
    
    # Check if n is a power of 2
    return n & (n - 1) != 0

for i in range(input_count):
    x = int(input())
    if has_odd_divisor(x):
        result.append("YES")
    else:
        result.append("NO")
        
for i in result:
    print(i)
