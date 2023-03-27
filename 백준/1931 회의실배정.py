def perm(i, k):
    
    if i == k:
        maxV = 0
        if maxV < len(p):
            maxV = len(p)


N = int(input())

lst = []    # 각 회의시간 리스트에 담기
for tc in range(N):
    start, end = map(int, input().split())
    lst.append((start, end))
print(lst)

# 여기서 하나씩 꺼내서 순열돌리기
num = len(lst)  # 리스트안에 들어가 있는 갯수
p = [0] * num   # 나타낼 값
used = [0] * num    # 방문체크
perm(0, num)

