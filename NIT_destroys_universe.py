import collections


import collections
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    if len(set(a)) == 1 and a[0] == 0:
        print("0\n")
        continue

    a = collections.deque(a)

    while a and a[-1] == 0:
        a.pop()
    while a and a[0] == 0:
        a.popleft()

    if 0 in a:
        print("2\n")
    else:
        print("1\n")
