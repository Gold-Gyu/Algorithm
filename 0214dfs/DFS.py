def dfs(s, V): # s 시작, V 정점 개수

    #초기화
    visited = [0] * (V + 1) # V + 1의 의미는 인덱스 0번은 그대로 두겠다라는 의미 # 왜 0번 인덱스는 그대로 두는거죠??

    stack = []

    # 현재 방문 정점 i
    i = s
    visited[i] = 1
    print(i)

    while True:
        """
        인접리스트를 사용할 떄
        for w in adjL[i]:
        if visited[w] == 0:
            stack.append(w)
            i = w
            visited[w] = 1
            print(node[i])
            break
        """
        # 현재 정점 i 에서 선택할 수 있는 다음 정점 w에 대해서
        # 1. w로 가는 길이 있고 2. w를 만난(방문한)적이 없다면(visited로 확인) w를 방문
        for w in range(1, V+1): # for문이 다 돌아도 break이 안나면 else로 넘어간다. # 시작점에서 넘어갈수 있는 정점 리스트 : w
            if adj[i][w] == 1 and visited[w] == 0:
                # w는 길이 있으니까 현재 위치 i 를 stack에 저장
                stack.append(i)
                # 현재위치 i를 다음 위치 w로 변경 (i가 w로 이동)
                i = w
                print(i)
                # w는 방문했다 라고 표시
                visited[w] = 1
                # 현재 위치 i 에서 더 갈 필요(확인할 필요) 가 없으므로
                break # 종료함. # 다시 i, w의 값을 가지고 while로 돌아간다.


        # 내가 i에서 탐색해봤을 때 더 이상 탐색할 곳이 없다면
        else:
            # 내가 최근에 방문했떤 정점을 스택에 넣어놓았었으니, 그걸 꺼내서 그 위치로 돌아가야한다.
            if stack: # stack이 true라면, 길이가 0이 아니라면, 비어있지않다면
               i = stack.pop() # 여기서 끝나고 다시 stack과 i 갱신해서 while문으로 간다


            # 스택이 비어있는 경우, 더 이상 stack에서 뺄게 없는 경우 : 탐색 종료
            else:
                break # while문 끝하고 그 라인의 return 값

    # 함수 종료전에 할 일
    return # 없으므로 종료

# w로 가는 길이 있다는 걸 알아내는법, 어떻게 판단하는가
# 1. 인접행렬
# 1 - 1 : 방향없는 그래프면 전치했을 떄 같은 그림
    # x A B C D E F G
adj = [[0, 0, 0, 0, 0, 0 , 0, 0], # x
       [0, 0, 1, 1, 0, 0 , 0, 0], # A
       [0, 1, 0, 0, 1, 1 , 0, 0], # B
       [0, 1, 0, 0, 0, 1 , 0, 0], # C
       [0, 0, 1, 0, 0, 0 , 1, 0], # D
       [0, 0, 1, 1, 0, 0 , 1, 0], # E
       [0, 0, 0, 0, 1, 1 , 0, 1], # F
       [0, 0, 0, 0, 0, 0 , 1, 0]] # G

node = ["", "A", "B", "C", "D", "E", "F", "G"]

"""
이걸 통해 인접 정렬 만들 것
정점의 개수, 간선의 개수(꼭지점을 이어주는 길의 개수)
(V, E)
7, 8
간선에 대한 정보(start, to)
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7


V, E = map(int(input())
adj = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    start, to = map(int, input().split())
    adj[start][to] = 1
    # 무향 그래프(방향이 없는 그래프만 아래 추가)
    adj[to][start] = 1



"""




"""
# 2. 인접리스트 adjL[i] : i 번 정점에 연결되어있는 정점들의 리스트

V, E = map(int(input())
adjL = [[] for _ in range(V + 1)]
for i in range(E):
    start, to = map(int, input().split())
    adjL[start].append(to)
    adjL[to].append(start)
"""
dfs(1, 7)