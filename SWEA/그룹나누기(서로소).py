import sys
sys.stdin = open("그룹나누기.txt", "r")

# 발표자가 몇명인지 세기

T = int(input())

# 집합 하나하나 만들어주기
def makeset(i):
    p[i] = i    # 집합 하나를 씩 만들어준다

# i가 속한 집합의 대표를 얻는 연산
def findset(i):
    if p[i] == i:
        return i
    else:
        return findset(p[i])

def union(x, y):
    p[findset(y)] = findset(x)

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    n = len(arr)
    p = [0] * (N+1)


    sset = set()

    # 집합 만들고
    for i in range(1, N+1):
        makeset(i)

    # 2개씩 짝 짓고
    for x in range(1, n, 2):
        union(arr[x], arr[x-1])

    # 이제 대표 찾고 중복되지 않은 것들을 출력한다.
    for i in range(1, N+1):
        sset.add(findset(i))

    print(f"#{tc} {len(sset)}")