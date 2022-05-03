#왕실의 나이트
#해답 참고한 문제

coor = input() #ex. a1
column = ord(coor[0]) - ord('a') + 1 #열. 왜 이렇게 ..?
row = int(coor[1]) #행
count = 0

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

for data in steps:
    #각 방향에 대해 갈 수 있는지 체크.
    x = column + data[0]
    y = row + data[1]
    if x >= 1 and y >= 1 and x <= 8 and y <= 8:
        count += 1

#print result
print(count)