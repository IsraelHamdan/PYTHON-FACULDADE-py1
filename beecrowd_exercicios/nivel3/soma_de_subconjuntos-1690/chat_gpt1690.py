t = range(int(input()))

for teste in t:
    n = int(input())
    entrada = input().split()
    a = [int(i) for i in entrada]
    s = 1
    for i in range(n):
        if a[i] <= s:
            s += a[i]
        else:
            break
    print(s)

 