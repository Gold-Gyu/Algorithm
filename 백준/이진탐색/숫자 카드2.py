# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10


given_num = int(input())
given_lst = list(map(int, input().split()))
get_num = int(input())
get_lst = list(map(int, input().split()))
arr = sorted(given_lst)
answer = {}

for i in given_lst:
  if i in answer:
    answer[i] += 1
  else:
    answer[i] = 1

for i in get_lst:
  if i in answer:
    print(answer[i], end=" ")
  else:
    print(0, end=" ")

