lst = [33, 21, 270, 3, 66]
n = len(lst)


for i in range(n-1, 0, -1): # 각 구간의 끝
    for j in range(i):  # 비교할 왼쪽 원소
        if lst[j] > lst[j+1]: # 왼쪽에 더 큰 값이 있으면
            lst[j], lst[j+1] = lst[j+1], lst[j] # 오른쪽과 자리를 바꾼다.

print(lst)