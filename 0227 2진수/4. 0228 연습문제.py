"""

01D06079861D79F99F

"""
# 16진수를 2진수로 나타내기
arr = input()
for x in arr:
    num = int(x, 16)    # 16진수를 10진수로 만들기


    for j in range(3, -1, -1):
        bit = 1 if num&(1<<j) else 0    # num의 j번째 비트가가 1인지 아닌지 파악
        print(bit, end = "")
    print(" ", end = "")