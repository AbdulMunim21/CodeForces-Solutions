grid = input().split(" ")
horizontal_sticks = int(grid[0])
vertical_sticks = int(grid[1])

result = {
    True: "Akshat",
    False: "Malvika"
}

boy_turn = True
while horizontal_sticks > 0 and vertical_sticks > 0:
    horizontal_sticks -= 1
    vertical_sticks -= 1
    boy_turn = not boy_turn
    
print(result[not boy_turn])
