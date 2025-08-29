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

# A 범위(오프셋 적용)
Ax1, Ax2 = sorted((x1[0] + offset, x2[0] + offset))
Ay1, Ay2 = sorted((y1[0] + offset, y2[0] + offset))

# A-only(값==1) 셀들의 최소/최대 행·열 찾기
found = False
min_row, max_row = 10**9, -1
min_col, max_col = 10**9, -1

for r in range(Ay1, Ay2):
    for c in range(Ax1, Ax2):
        if grid[r][c] == 1:       # A만 칠해진 칸
            found = True
            if r < min_row: min_row = r
            if r > max_row: max_row = r
            if c < min_col: min_col = c
            if c > max_col: max_col = c

if not found:
    print(0)                      # A가 B에 완전히 덮였으면 0
else:
    # 최소 덮개 직사각형(격자 기준): +1 중요 (half-open로 채웠기 때문)
    width  = max_col - min_col + 1
    height = max_row - min_row + 1
    print(width * height)