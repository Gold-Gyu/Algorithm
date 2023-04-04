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

# 함수가 시작할 때 필요한 것들
# 1. 임의 시작점을 정해서 시작한다.
# s : 시작정점
# V :정점의 개수
# 서로소 인 2개의 집합 정보를 유지
# => 일종의 visited배열
def prim(s, V):
    MST = [0] * (V+1)   # 내가만든 MST에 포함이 되는지 확인
    MST[s] = 1  # 시작점 방문체크

    # MST 가중치 합
    maxV = 0

    for i in range(V):  # V번 반복하는 이유 : 우리가 최소 V개의 정점을 연결할 것이기 떄문에
        u = 0   # 어떤 정점과 연결된 다른 정점들 중에서 최소 가중치를 가진 정점
        minV = 10000 #연결된 정점중 최소 가중치를 찾을 것이다.

        # MST에 포함된 정점 i가 있다고 할 때 이 i와 인접한 정점이 j가 있다고 쳐보자
        # 정점 i, j가 MST에 포함되지 않고
        # 가중치가 최소인 정점 u를 찾기

        for i in range(V+1):
            # MST에 포함된 i를 찾아야한다.
            if MST[i] == 1: # 1이면 포함되어있다.
                # 포함되어있다면 인접해있는 j를 찾는다.
                for j in range(V+1):    # i와 인접해 있는 j 값들을 다 둘러보면서 가장 가중치가 작은 것을 찾는다.
                    # i와 j가 연결되어있고
                    # j는 지금까지 내가 만든 트리에 포함 x
                    # 새로 연결할 j는 최소 가중치를 가진다면
                    if adjm[i][j] > 0 and MST[j] == 0 and minV > adjm[i][j]:
                        u = j   # j가 최소 가중치를 가지고 있는 인접한 정점이다.
                        minV = adjm[i][j]   # 최소 가중치를 찾음

        maxV += minV
        MST[u] = 1

    return maxV



V, E = map(int, input().split())
adjm = [[0] * (V+1) for _ in range(V+1)]

# 인접 행렬
# 가중치가 있는 무방향 그래프
for _ in range(E):
    s, e, w = map(int, input().split())
    adjm[s][e] = w
    adjm[e][s] = w
print(prim(0, V))
