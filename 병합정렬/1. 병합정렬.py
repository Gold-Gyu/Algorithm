def merge(left, right):
    pass





def msort(s, e):

    if s == e:  # 하나 짜리라면 끝
        return  # l과 r이라는 인덱스를 받았기 떄문에 원본

    m = (s+e)//2    # 중간지점
    msort(s, m) # l~ m 까지 정렬해놔
    msort(m+1, e)    # m+1 부터 r까지 정렬을 해놔

    k = 0   # 임시저장소 tmp에 저장하려고할 때 tmp인덱스를 나타냄
    l, r = s, m+1 # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치

    while l <= m or r <= e: # 왼쪽의 맨끝 이하거나 오른쪽의 맨 끝 이하면 계속 반복
        if l <= m and r <= e:    #
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1

        elif l <= m:    # 왼쪽만 범위안에 남아있고 오른쪽은 범위를 벗어났다면
            while l <= m:
                tmp[k] = arr[l]
                l += 1
                k += 1

        elif r <= m:
            while r <= e:
                tmp[k] = arr[r]
                r += 1
                k += 1

        # 임시저장소 tmp에 저장해둔 것을 되돌리는 과정 필수 !!! ★★
        # arr에 다시 덮어쓰기

    i = 0
    while i < k:
        arr[s + i] = tmp[i]
    return



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N   # 이거 왜 만든거임? => 좌랑 우에서 정렬해서 가져올 임시 저장소

    msort(0, N-1)   # 0부터 N-1구간까지 정렬을 해봐라
    print(arr)