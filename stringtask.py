string = input()

new_string = ""
for i in string:
    if (i == "a" or i == "A") or (i == "y" or i == "Y") or (i == "e" or i == "E") or (i == "i" or i == "I") or (i == "o" or i == "O") or (i == "u" or i == "U"):
        pass
    else:
        new_string = new_string + "."+i.lower()

print(new_string)   
