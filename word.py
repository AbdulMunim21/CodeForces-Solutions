word = input()

small_letters_length = 0
big_letters_length = 0

for i in word:
    if i.islower():
        small_letters_length += 1
    else:
        big_letters_length += 1

if small_letters_length >= big_letters_length:
    print(word.lower())
else:
    print(word.upper())
