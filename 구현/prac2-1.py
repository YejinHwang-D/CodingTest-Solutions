#상하좌우

n = int(input())
order = input().split()
x = 1; y = 1

for data in order:
    if data == 'L':
        if y >= 2:
            y -= 1
    elif data == 'R':
        if y <= n-1:
            y += 1
    elif data == 'U':
        if x >= 2:
            x -= 1
    elif data == 'D':
        if x <= n-1:
            x += 1
print(x, y)