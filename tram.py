stops = eval(input())

minimum_capacity = []
people_at_stop = 0

for i in range(stops):
    people = input()
    people = people.split(" ")
    leaving = int(people[0])
    arriving = int(people[1])
    people_at_stop -= leaving
    people_at_stop += arriving
    minimum_capacity.append(people_at_stop)

minimum_capacity.sort()
print(minimum_capacity[-1])
