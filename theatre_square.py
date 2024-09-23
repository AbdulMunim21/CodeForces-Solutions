import math

value_input = input().split(" ")
n = int(value_input[0]) 
m = int(value_input[1]) 
a = int(value_input[2])

flagstones_along_width = math.ceil(n / a)
flagstones_along_height = math.ceil(m / a)

total_flagstones = flagstones_along_width * flagstones_along_height

print(total_flagstones)
