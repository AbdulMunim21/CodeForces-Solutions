username = input()
distinct_characters = []


for i in username:
    if i not in distinct_characters:
        distinct_characters.append(i)

if len(distinct_characters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")