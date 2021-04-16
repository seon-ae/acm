from itertools import combinations

n, m = map(int, input().split())
board=[list(map(int,input().split())) for _ in range(n)]

houses=[]
chickens=[]
for i in range(n):
  for j in range(n):
    if board[i][j]==1: houses.append([i,j])
    if board[i][j]==2: chickens.append([i,j])

minimum=float('inf')
combi_arr=combinations(chickens, m)
for choice in combi_arr:
  distance_ctoh=0
  for house in houses:
    distance_ctoh+=min([abs(house[0]-shop[0])+abs(house[1]-shop[1]) for shop in choice])
    # 치킨거리의 합이 이전 치킨거리값의 합보다 크다면 더이상 볼 필요x
    if minimum<=distance_ctoh: break
  #치킨집 조합을 바꿨을 때 치킨거리합이 더 작은 경우
  if distance_ctoh<minimum: minimum=distance_ctoh

print(minimum)
