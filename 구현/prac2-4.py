#게임 개발
#교재 예제 참고
#dx, dy 유용하다는 개념 습득

n, m  = map(int, input().split())
a, b, d = map(int, input().split()) #d는 북(0) 동(1) 남(2) 서(3)

temp = [[0]*m for _ in range(n)]
temp[a][b] = 1 #캐릭터 서있는 자리 표시
count = 1

area = []
for i in range(n):
    row = list(map(int, input().split()))
    area.append(row)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1: #북,동,남,서 순서인데 0인 북에서 왼쪽은 서쪽 ~ 
        d = 3 #서쪽

turn_time = 0 #네방향 모두 못갈 경우 체크용
while True:
    turn_left()
    nx = a + dx[d] #현재 방향에 따라 증감
    ny = b + dy[d]
    if temp[nx][ny] == 0 and area[nx][ny] == 0: #가보지 않았고, 육지라면?
        temp[nx][ny] = 1 #방문
        a = nx
        b = ny
        count += 1
        turn_time = 0 #다시 초기화
        continue
    else:
        turn_time += 1
    if turn_time == 4: #4방향 모두 못갈 때
        nx = a - dx[d] #되돌리기
        ny = b - dy[d]
        if area[nx][ny] == 0: #육지면 이동
            a = nx
            b = ny 
        else: #이것마저도 바다야?
            break
        turn_time = 0

print(count)