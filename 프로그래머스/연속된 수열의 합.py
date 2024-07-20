def solution(sequence, k):
    right = left = 0

    size = len(sequence)
    answer = [0, len(sequence)]
    numSum = sequence[0]

    while True:
        if numSum < k:
            right += 1
            if right == size:
                break
            numSum += sequence[right]

        else:

            if numSum == k:
                if right - left < answer[1] - answer[0]:
                    answer = [left, right]
            numSum -= sequence[left]
            left += 1

    return answer