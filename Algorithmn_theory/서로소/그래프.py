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



V, E = map(int, input().split()) # 0 ~ v 정점 번호, E 간선수


def findset(x): # x가 속한 집합의 대표 원소를 찾는다
   # 누가 대표원소일까
    while rep[x] != x:  # x == rep[x]가 될 때 까지 반복
        rep[x] = x
    return x

def union(x, y):    # y의 대표원소가 x의 대표원소를 가르키도록 즉, x라는 대표원소 안으로 y가 들어가는것임.
    rep[findset(y)] = findset(x)
    # y가 속한 대표원소를 찾아가봐

# makeset()
rep = [i for i in range(V+1)]
graph = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append([v1, v2, w])

# 1번째 단계 가중치 기준 오름차순 정렬
graph.sort(key=lambda x:x[2]) # w를 기준으로 정렬
# print(graph)

# 2 N개 정점(V+1), N-1개의 간선 선택
N = V + 1
s = 0 # mst에 포함된 간선의 가중치 합
cnt = 0

MST = []    # mst 구성요소 확인하기 위해
# 가중치가 작은 것부터 순서대로 꺼내온다....
for u, v, w in graph:
    # 두개의 대표원소를 찾는다.
    # 두개의 대표원소 비교
    if findset(u) != findset(v):    # 사이클이 생기지 않음
        cnt += 1
        s += w  # 가중치 합
        MST.append([u,v,w])
        union(u, v) # 사이클이 생기는걸 확인할 수 있음
        if cnt == N-1: # MST 구성완료
            break
print(s)
print(MST)