rooms = int(input())
accomadation_room = 0

for i in range(rooms):
    x = input().split(" ")
    p = int(x[0])
    q = int(x[1])
    if q - p >= 2:
        accomadation_room += 1

print(accomadation_room)