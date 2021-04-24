from collections import deque
arr=[input() for _ in range(4)]
k=int(input())
q=deque()
cparr=[]

# input
for _ in range(k):
    num,dire=map(int,input().split())
    q.append([num-1,dire])

# copy arr
for i in range(4):
    cparr.append(arr[i])

# 톱니바퀴별로 맞닿은 부분의 정보.
info=dict()
info[0],info[1],info[2],info[3]=(0,int(arr[0][2])),(int(arr[1][6]),int(arr[1][2])),(int(arr[2][6]),int(arr[2][2])),(int(arr[3][6]),0)

def wrap_around(arr,dire):
    tmp_arr=""
    if dire==1:
        tmp_arr+=(arr[7]+arr[0:7])
        return tmp_arr
    elif dire==-1:
        tmp_arr+=(arr[1:8]+arr[0])
        return tmp_arr
while q:
    num,dire=q.popleft()
    #양옆에 바퀴를 검사해서 돌아가야된다면(극이 다르다면) 큐에 넣음
    miniq=deque()
    miniq.append([num,dire])
    visited=[0]*4
    while miniq:
        num,dire=miniq.popleft()
        cparr[num]=wrap_around(cparr[num],dire)
        if 0<num<3 :
            visited[num]=1
            if info[num-1][1]!=info[num][0] and not visited[num-1]:
                miniq.append([num-1,dire*(-1)])
            if info[num+1][0]!=info[num][1] and not visited[num+1]:
                miniq.append([num+1,dire*(-1)])
        elif num==0 and not visited[1]:
            visited[0]=1
            if info[0][1]!=info[1][0]:
                dire=dire*-1
                miniq.append([1,dire])
        elif num==3 and not visited[2]:
            visited[3]=1
            if info[2][1]!=info[3][0]:
                dire=dire*-1
                miniq.append([2,dire])

    # info 최신화
    for num in range(0,4):
        info[num]=(cparr[num][6],cparr[num][2])

total=0
for idx in range(4):
    if cparr[idx][0]=='0':
        continue
    else:
        if idx==0:
            total+=1
        elif idx==1:
            total+=2
        elif idx==2:
            total+=4
        elif idx==3:
            total+=8

print(total)