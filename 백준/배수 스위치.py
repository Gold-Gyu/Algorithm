lst = [0] + list(input())
n = len(lst)
cnt = 0
flag = False
for i in range(1, n):
    if lst[i] == "Y":
        for j in range(i, n, i):
            if lst[j] == "N":
                lst[j] = "Y"
            elif lst[j] == "Y":
                lst[j] = "N"
        cnt += 1

        count = 0
        for k in range(1, n):
            if lst[k] == "N":
                count += 1
                if count == n - 1:
                    flag = True
                    break # for k
        if flag:
            break # for i
for i in lst:
    if i == "Y":
        cnt = -1
print(cnt)
