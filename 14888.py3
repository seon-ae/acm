from itertools import combinations
from itertools import permutations
from collections import deque
n=int(input())
arr=list(map(int,input().split()))
opr=list(map(int,input().split())) #덧셈, 뺄셈, 곱셈, 나눗셈
pocket=[]
q=deque()
for i in arr:
    q.append(i)
for idx in range(4):
    if opr[idx]!=0:
        while opr[idx]>0:
            pocket.append(idx)
            opr[idx]-=1
combiset=list(permutations(pocket))
result=[]
tmpq=deque()
#복사
for i in range(n):
    tmpq.append(q[i])

for combi in combiset:
    total=0
    opr1 = tmpq.popleft()
    for operator in combi:
        opr2=tmpq.popleft()
        if operator==0:
            total=(opr1+opr2)
        elif operator==1:
            total=(opr1-opr2)
        elif operator==2:
            total=(opr1*opr2)
        elif operator==3:
            if opr1<0:
                total=-(abs(opr1)//opr2)
            else:
                total=(opr1//opr2)
        opr1=total

    result.append(total)
    #queue가 empty한 상태이니 다시 복사
    for i in range(0,n):
        tmpq.append(q[i])

result.sort()
print(result[len(result)-1])
print(result[0])