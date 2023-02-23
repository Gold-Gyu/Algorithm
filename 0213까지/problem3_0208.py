# 숫자를 문자로 바꾸는 법

def itoa(num):
    ret = ""

    # 숫자 하니씩 가져와서(일의 자리부터 문자열로 바꾸기
    while num > 0:
        i = num % 10
        ret += chr(ord("0") + i) # 0의 아스키코드 :48
        num //= 10

    return ret[::-1]


print(type(itoa(123)))
print(itoa(123))