def can_say_hello(s):
    # Define the target word
    target = "hello"
    target_index = 0

    # Iterate through the characters in the input string
    for char in s:
        # Check if the current character matches the target character
        if char == target[target_index]:
            target_index += 1

        # If all characters in 'hello' are matched, return True
        if target_index == len(target):
            return "YES"

    # If the loop finishes without matching all characters, return NO
    return "NO"

# Example usage
s = input()
print(can_say_hello(s))
