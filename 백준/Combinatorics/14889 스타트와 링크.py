
# 가능한 모든 조합 계산
# 함수 호출을 자주하는 것 <<< 최대한 함수 호출 적게하는 것

def dfs(idx, A, B):
    global minV
    # # 가지치기 : 이미 0이면 더 이상할 필요 없음
    if minV == 0:
        return

    # 한팀이 m명 초과인 경우
    if len(A) > m or len(B) > m:
        return

    # 종료조건
    if idx == n:
        # 정답처리
        if len(A) == m and len(B) == m:
            asm = bsm = 0
            for i in range(m):
                for j in range(m):
                    asm += arr[A[i]][A[j]]
                    bsm += arr[B[i]][B[j]]
            minV = min(minV, abs(asm-bsm))
        return

    # 1팀 선택
    dfs(idx+1, A+[idx], B)
    # 2팀 선택
    dfs(idx+1, A, B+[idx])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = n//2
minV = 999999

dfs(0, [], [])

print(minV)