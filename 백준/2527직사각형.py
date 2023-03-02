for tc in range(4):
    x1, y1, x2, y2, i1, j1, i2, j2 = map(int, input().split())
    # if (x1 <= i1 < x2 and y1 <= j1 < y2) or (x1 < i2 < x2 and y1 < j2 < y2):
    #     print("a")
    if (x1 < i1 < x2 and y1 < j1 < y2) or (i1 < x1 < i2 and j1 < y1 < j2):
        print("a")
    if (x1 >= i2 and y1 <= j2) or (x1 <= i2 and y2 >= j2) or (x1 <= i1 and y2 >= j1) or (x2 <= i1 and y2 >= j1):
        print("b")


