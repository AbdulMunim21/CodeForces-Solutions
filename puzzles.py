first_input = input().split(" ")
students = int(first_input[0])
puzzles = int(first_input[1])

quantities = input().split(" ")
quantities = [int(value) for value in quantities]
quantities.sort()

index = students - 1
starting_index = 0
result = [] 
while index < len(quantities):
    value = int(quantities[index]) - int(quantities[starting_index])
    result.append(value)
    index += 1
    starting_index += 1

result.sort()
print(abs(result[0]))
