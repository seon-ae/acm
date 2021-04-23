from heapq import heappush, heappop
n=int(input())
path=[[0]*n for _ in range(n)]
q=[]
distance=0
eat=0
body=2
arr=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
  for j in range(n):
    if arr[i][j]==9:
      heappush(q,[0,i,j])
      arr[i][j]=0

while q:
  d,y,x=heappop(q)
  if arr[y][x]<body and arr[y][x]!=0:
    eat+=1
    arr[y][x]=0
    if eat==body:
      eat=0
      body+=1
    distance+=d
    q=[]
    path=[[0]*n for _ in range(n)]
    d=0

  for dy,dx in (-1,0),(0,1),(1,0),(0,-1):
    nd,ny,nx=d+1,y+dy,x+dx
    if ny<0 or ny>=n or nx<0 or nx>=n:
      continue
    if arr[ny][nx]>body or path[ny][nx]:
      continue
    path[ny][nx]=1
    heappush(q,[nd,ny,nx])
print(distance)