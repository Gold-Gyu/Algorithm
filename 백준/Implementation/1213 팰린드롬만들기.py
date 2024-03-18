from collections import Counter
import sys

# Insight : 회문은 글자 중에 갯수가 홀수인 것이 2개 이상이면 만들 수 없다!!!
n = list(map(str, sys.stdin.readline().strip()))
n.sort()
check =Counter(n)
answer_lst = []
cnt = 0
center = ""

# print(check)

for i in check:
  if check[i] % 2 != 0:
    cnt += 1
    # 홀수인 값을 받아준다.
    center += i
    n.remove(i)
    # print("n : ", n)

  if cnt > 1:
    break

if cnt > 1:
  print("I'm Sorry Hansoo")
else:
  res = ""
    # 반복문을 통해 팰린드롬을 반을 나누었을 때 왼쪽 부분을 더해준다.
  for i in range(0, len(n), 2):
    res += n[i]
    # print("i : ", i)

    # 왼쪽 + 가운데(홀수) + 오른쪽
  print(res + center + res[::-1])





