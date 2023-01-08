s = input()
t = input()

condition = True

if len(s) == len(t):
    for i in range(len(s)):
        if s[i] != t[len(s)-(i+1)]:
            condition = False
            break
else:
    condition = False

if condition :
    print("YES")
else:
    print("NO")
