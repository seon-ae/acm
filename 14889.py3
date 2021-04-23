from itertools import combinations
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
person=[i for i in range(n)]
half=n//2
start_team=list(combinations(person,half))
i=0
start_capacity=0
link_capacity=0
diff=987654321

for j in start_team:
    link_team = []
    link_capacity=0
    start_capacity=0
    for element in person:
        if element not in j:
            link_team.append(element)
    start_two=list(combinations(j,2))
    for y,x in start_two:
        start_capacity+=arr[y][x]
        start_capacity+=arr[x][y]

    link_two=list(combinations(link_team,2))
    for y,x in link_two:
        link_capacity+=arr[y][x]
        link_capacity+=arr[x][y]
    diff=min(diff,abs(start_capacity-link_capacity))
print(diff)

