# 이 정사각형에서 꼭짓점에 쓰여있는 숫자가 모두 같은 가장 큰 정사각형의 크기 => 정사각형임으로 한 변의 길이만 찾아서 * 2

# 1. 입력값을 잘 받는지 확인한다.
n, m = map(int, input().split())


numbers_lst = [list(map(int, input())) for _ in range(n)]

T = min(n, m)
print(T)
print(n, m)
print(numbers_lst)
if n == 1 or m == 1:
  print(1)
else:
  for i in range(n):
    for j in range(m):
      pass