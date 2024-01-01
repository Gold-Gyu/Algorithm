n = int(input())

lst = []
target_lst = []

for i in range(n):
    m = int(input())
    lst.append(m)

# * list안에서 첫 번째 값을 가장 크게 만들기 위해 숫자 이동의 최소값 구하기
#* 최솟값을 찾는 최적화된 알고리즘
cnt = 0
more_value_cnt = 0
same_value_cnt = 0
winner = lst[0]

for i in range(1, n):
    if winner < lst[i]:
        more_value_cnt += 1
        target_lst.append(lst[i])
    elif winner == lst[i]:
        same_value_cnt += 1

target_lst.sort()

if more_value_cnt == 0 and same_value_cnt == 0:
    print(0)
elif more_value_cnt == 0 and same_value_cnt > 0:
    print(1)
elif more_value_cnt > 0:
    
    while True:
        target_lst.sort(reverse=True)

        if winner > target_lst[0]:
            break

        val = target_lst.pop(0)
        val -= 1
        target_lst.append(val)
        winner += 1
        cnt += 1
    print(cnt)