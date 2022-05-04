#음료수 얼려 먹기

n, m = map(int, input().split())
arr = []
count = 0
for i in range(n):
    arr.append(list(map(int, input())))

#깊이 우선 탐색 사용
def dfs(x, y):
    if x<= -1 or x >= n or y <= -1 or y >= m:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)
        return True
    return False
        
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)