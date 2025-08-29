x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())  # A
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())  # B

offset = 1000
N = offset * 2 + 1
grid = [[0]*N for _ in range(N)]

# 두 사각형 채우기 (half-open)
for i in range(2):
    xa, xb = sorted((x1[i] + offset, x2[i] + offset))
    ya, yb = sorted((y1[i] + offset, y2[i] + offset))
    for row in range(ya, yb):
        for col in range(xa, xb):
            grid[row][col] += 1

# A의 경계(오프셋 적용 후)
Ax1, Ax2 = sorted((x1[0] + offset, x2[0] + offset))
Ay1, Ay2 = sorted((y1[0] + offset, y2[0] + offset))

x_max, y_max = 0, 0
for row in range(Ay1, Ay2):  
    if any(cell == 1 for cell in grid[row]):
        y_max = row

    for col in range(Ax1, Ax2):
        if(grid[row][col] == 1 and x_max <= col):
            x_max = col 

# print("x_max",x_max,"y_max",y_max)
# 'A만 칠해진' 칸만 카운트 (겹친 곳은 2가 되므로 제외)
area = 0
for row in range(Ay1, y_max + 1):      # y축 → 행
    for col in range(Ax1, x_max + 1):  # x축 → 열
        # print(grid[row][col], end=" ")
        if(grid[row][col] >= 1):
            area += 1
    # print()

print(area)