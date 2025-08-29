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

width_max = 0
height = Ay2 - Ay1
for row in range(Ay1, Ay2):
    width_count = 0 
    for col in range(Ax1, Ax2):
        if(grid[row][col] == 1):
            width_count += 1
        else:
            width_count = 0 

        if all(x == 2 for x in grid[row]):
            height -= 1
    
    width_max = max(width_max,width_count)


area = width_max * height
print(area)