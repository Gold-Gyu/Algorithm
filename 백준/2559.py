N, M = map(int, input().split())
lst = list(map(int, input().split()))

a = sum(lst[:M])
maxV = a
for i in range(1, N-(M-1)):
    a = a - lst[i-1] + lst[M - 1 + i]
    if maxV < a:
        maxV = a
print(maxV)




