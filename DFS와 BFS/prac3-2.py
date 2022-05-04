#미로 탈출
#끝까지 전혀 이해안돼서 책의 코드 분석함
from collections import deque

n, m = map(int, input().split())
arr = []

dx = [0, 0, -1, 1] #상하좌우
dy = [1, -1, 0, 0]

for i in range(n):
    arr.append(list(map(int, input())))

#탈출 알고리즘은 BFS 이용
def bfs(x, y):
    q = deque()
    q.append((x, y)) #시작 위치 기록
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0: #괴물 있는 부분이면
                continue
            elif arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1 #이전 노드 + 1
                q.append((nx,ny))
    return arr[n-1][m-1] #맨 오른쪽 아래에 기록된 최단거리 반환

print(bfs(0, 0))