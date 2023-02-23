# 1. 빈 문자열 만들고 뒤에서부터 이어붙이는 방법
"""
def my_reverse(string):
    ret = ""
    n = len(string)

    for i in range(n-1, -1, -1):
        ret += string[i]

"""

# 앞뒤로 차례대로 바꾸는 방법

def my_reverse(string):


    s2 = list(string)
    n = len(s2)

    for i in range(n // 2):
        s2[i], s2[n - i - 1] = s2[n - i - 1], s2[i]

    print(s2)
    return "".join(s2)

print(my_reverse("reverse this strings"))


