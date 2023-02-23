lst = ["a","b","c","c"]

text = "abcd"

stack = []
cnt = 0 # 남은 글자수 세기
for c in lst:
    if c in text:
        stack.append(c)

        print(stack)



