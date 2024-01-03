"""
1. n개 수둘의 합 n으로 나눈것
2. 중앙값
3. 가장많이 나타난 것

"""
from collections import Counter

n = int(input())

val = 0
lst = []
countset = {}
for i in range(n):
  lst.append(int(input()))
  val += lst[i]

lst.sort()
counter = Counter(lst)
sorted_counter = sorted(counter.items(), key = lambda item: item[1], reverse=True)
# final_sorted_counter = sorted(sorted_counter, key = lambda item: item[1], reverse=True)
max_key = max(lst, key = counter.get)

# 1 산술평균
print(round(val / n))
# 2 중앙값
print(lst[n//2])
# 3 최빈값
if n == 1:
  print(lst[0])
elif sorted_counter[0][1] == sorted_counter[1][1]:
  print(sorted_counter[1][0])
else:
  print(sorted_counter[0][0])
# 4 범위
print(lst[-1] - lst[0])


"""
import sys

n= int(input())
dic={}
li=[]
for i in range(n):
    a=int(sys.stdin.readline().strip())
    li.append(a)
    if a in dic:
        dic[a]+=1
    else:
        dic[a]=1
li.sort()
sdic=sorted(dic.items(),key=lambda x:(-x[1],x[0]))
if len(sdic)>1:
    fq= sdic[1][0] if sdic[0][1]==sdic[1][1] else sdic[0][0]
else:
    fq= sdic[0][0]
print(int(round(sum(li)/n)),li[len(li)//2],fq,max(li)-min(li), sep='\n')


"""