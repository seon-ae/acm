n=int(input())
score=[]
for _ in range(n):
    score.append(int(input()))
memo=[0]*n

if (len(score)==1):
    print(score[0])
elif (len(score)==2):
    print(score[0]+score[1])
else:
    memo[0]=score[0]
    memo[1]=score[1]+score[0]
    memo[2]=max(score[0]+score[2],score[1]+score[2])

    for i in range(3,n):
        memo[i]=max(score[i]+memo[i-2],score[i]+score[i-1]+memo[i-3])

    print(memo.pop())

