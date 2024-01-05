txt = input()

size = len(txt)
cnt = 0
lst = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
check = [0] * size
for idx in range(size):
  if idx < size-1 and check[idx] == 0 and (txt[idx] + txt[idx+1]) in lst:
    check[idx] += 1
    check[idx + 1] += 1
    cnt += 1
  elif idx < size-2 and check[idx] == 0 and (txt[idx] + txt[idx+1] + txt[idx+2]) == "dz=":
    check[idx] += 1
    check[idx + 1] += 1
    check[idx + 2] += 1
    cnt += 1
  elif check[idx] == 0:
    check[idx] += 1
    cnt += 1
  # print(check)

print(cnt)
