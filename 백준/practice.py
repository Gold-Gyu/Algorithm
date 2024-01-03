n = int(input())
dic = {}
lst = []
for i in range(n):
    num = int(input())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
print(dic)