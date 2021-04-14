from collections import deque
n=int(input())
k=int(input())
queue=deque(input().split())
photo=deque()
frequency={}
for i in range(101):
    frequency[i]=0 #빈도수 초기화

for _ in range(k):
    student=int(queue.popleft())
    if student in photo: #학생사진이 이미 걸려있을 때 빈도 증가시키기
        frequency[student]+=1
    else: # 걸려있지 않을때
        if len(photo)==n: #빈자리가 없을 때
            vals=[]
            for j in photo:
                vals.append(frequency[j])
            minv=min(vals)
            for i in photo:
                if frequency[i]==minv:
                    frequency[i]=0
                    photo.remove(i)
                    break
            photo.append(student)
            frequency[student]+=1
        else: #빈자리가 있을 때
            photo.append(student)
            frequency[student]+=1
ans=[]
for i in photo:
    ans.append(i)
ans.sort()
for i in ans:
    print (i, end=" ")