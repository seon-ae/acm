from collections import deque
n,m=map(int,input().split())
r,c,d=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
dir=[(-1,0),(0,1),(1,0),(0,-1)] #북,동,남,서
q=deque()
cnt=0 #청소한 방의 개수
q.append([r,c])

while q:
    r,c=q.popleft()
    flag=0
    if arr[r][c]==0:
        cnt+=1
        arr[r][c]=2 #청소한다.

    for i in range(4):
        d=(d+3)%4 #초기 방향에서 왼쪽부터 탐색해나갸아함
        nr,nc=r+dir[d][0],c+dir[d][1]
        if nr<1 or nc<1 or nr>=n-1 or nc>=m-1:
            continue
        if arr[nr][nc]==1 or arr[nr][nc]==2:
            continue
        q.append([nr,nc])
        flag=1
        break
    #네 방향 모두 탐색하였을떼

    if (flag==0):
        tmpd=(d+2)%4
        nr,nc=r+dir[tmpd][0],c+dir[tmpd][1]
        # 1.후진 불가능한 상황
        if arr[nr][nc]==1:
            print(cnt)
            exit(0)
        #2. 후진 가능한 상황
        if arr[nr][nc]==2:
            q.append([nr,nc])
print(cnt)
