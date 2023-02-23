'''
7
7 2 5 3 4 6 4
'''

N = int(input())

arr = list(map(int, input().split()))


for i in range(N-1):    # 작업 구간의 시작점. 기준인덱스 0 ~ N - 2까지
    minidx = i          # 맨 앞이 최소라 가정

    for j in range(i+1, N): # N-1까지
        if arr[minidx] > arr[j]: # 기준점에서 값과 비교값을 비교했을 때 기준점이 더 크다면..
            minidx = j # 기준점 인덱스 = j 인덱스
        

    arr[i], arr[minidx] = arr[minidx], arr[i]

print(arr)