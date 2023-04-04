"""

6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51

"""

rep = []

def findset(x):
    while x != rep[x]:
        x = rep[x]

    return x

def union(x, y):
    rep[findset(y)] = findset(x)


V, E = map(int, input().split())
edge = []

for i in range(E):
    s, e, w = map(int, input().split())
    edge.append([w, s, e])

edge.sort() # 가장 맨 앞 요소를 기준으로 정렬

# 대표 배열
rep = [i for i in range(V+1)]

# 내가 지금까지 선택한 간선의 개수
cnt = 0
# 지금까지 만든 MST의 가중치의 합
total = 0
# MST의 간선수 N = 정점수 - 1
N = V + 1
for w, s, e in edge:
    # s 집합의 대표와 e 집합의 대표가 달라야 사이클이 x
    # 사이클이 없다??
    if findset(s) != findset(e):    # 두개의 대표가 달라야 더해줄수 있음
        cnt += 1
        # 더한 후 병합
        union(s, e)
        total += w

        if cnt == N - 1: # cnt가 간선의 수만큼 되면 끝난다.
            break

print(total)