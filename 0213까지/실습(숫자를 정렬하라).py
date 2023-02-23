import sys
sys.stdin = open('input (8).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int,input().split()))

    counts = [0] * (max(nums) + 1)
    temp = [0] * len(nums)

    # for i in nums:
    #     counts[i] += 1
    # print(counts)
    for x in range(len(nums)):
        counts[nums[x]] += 1


    for i in range(1, len(counts)):
        counts[i] += counts[i-1]


    for i in range(len(temp)-1, -1, -1):
        counts[nums[i]] -= 1
        temp[counts[nums[i]]] = nums[i]

    temp2 = ' '.join(map(str, temp))


    print(f'#{tc} {temp2}')
