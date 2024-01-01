n = int(input())

# ! 동쪽 : 1 서쪽 : 2 남쪽 : 3 북쪽 : 4

lst = []
for i in range(6):
    direction, cm = map(int, input().split())
    lst.append([direction, cm])

lst1 = []
lst2 = []


for idx in lst:
    if idx[0] == 1:
        lst1.append(idx[1])
    elif idx[0] == 2:
        lst2.append(idx[1])
    elif idx[0] == 3:
        lst1.append(idx[1])
    else:
        lst2.append(idx[1])

 
ans = ((lst2[0] * lst2[1]) - (lst1[1] * lst1[2])) * n
print(ans)
