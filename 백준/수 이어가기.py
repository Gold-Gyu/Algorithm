
one = int(input())

greatlst = []
maxV = 0

for second in range(one-1, 0, -1):
    lst = []
    lst.append(one)
    lst.append(second)
    third = one - second
    if third > 0:
        lst.append(third)

        while True:
            second = second - third  # 4, 6, 8, 10
            if second < 0:

                break

            else:
                lst.append(second)
            third = third - second   # 5, 7, 9, 11
            if third < 0:
                flag = True
                break
            else:
                lst.append(third)

        if maxV < len(lst):
            maxV = len(lst)
            ans = lst
            # for i in range(maxV):
            #     greatlst.append(lst[i])


print(maxV)
print(*ans)




