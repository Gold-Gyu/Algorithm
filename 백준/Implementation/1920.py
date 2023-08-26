"""
5
4 1 5 2 3
5
1 3 7 9 5
"""

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target_arr = list(map(int, input().split()))
arr.sort()
# print(target_arr)

for target in target_arr:
    start = 0
    end = n -1
    
    flag = 0

    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            print(1)
            flag = 1
            break
      
        elif target > arr[mid]:
            start = mid + 1

        else:
            end = mid - 1


    if flag == 0:
        print(0)
