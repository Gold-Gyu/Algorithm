n = input()
print(n)

standard = { "w": 0, "o" : 0, "l" : 0, "f" : 0}
# 각 문자의 개수가 n개가 나란히 나오면 O
# 문자 두개를 이은것도 올바른단어
size = len(n)
for i in range(size):
