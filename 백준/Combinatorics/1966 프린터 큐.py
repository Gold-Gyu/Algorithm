"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    check = lst[m]
    num = 0
    flag = 0

    while True:
        for i in range(n):
            if lst[i] == max(lst):
                lst[i] = -1
                print(lst)
                num += 1
                if i == m:
                    flag = 1
                    break   # for i
        if flag:
            break
    print(num)
    # while True:
    #     if lst[0] == max(lst):
    #         ans = lst.pop(0)
    #         num += 1
    #         if ans == check and ans not in lst:
    #             break
            

    #     else:
    #         ans1 = lst.pop(0)
    #         print(lst)
    #         lst.append(ans1)
            
    # print(num)