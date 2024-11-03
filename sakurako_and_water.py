def solve():
    n = int(input())
    mn = dict()
    for i in range(n):
        a = [int(x) for x in input().split()]
        for j in range(n):
            mn[i - j] = min(a[j], mn.get(i - j, 0))
    ans = 0
    for value in mn.values():
        ans -= value
    print(ans)
 
t = int(input())
for _ in range(t):
    solve()