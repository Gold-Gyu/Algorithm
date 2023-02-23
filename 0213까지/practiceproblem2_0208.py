def simple_strcmp(s1, s2):


    # s1과 s2의 아스키 코드 값을 비교하여
    # 사전 순서 리턴 (앞서면 음수, 나중이면 양수)
    return ord(s1) - ord(s2)
print(simple_strcmp("A", "G"))