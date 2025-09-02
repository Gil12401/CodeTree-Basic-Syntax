n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
offset = 1000
N = offset * 2 + 1
grid = [[0]*N for _ in range(N)]

# red : odd
# blue : blue
for i in range(n):
    xa, xb = sorted((x1[i] + offset, x2[i] + offset))
    ya, yb = sorted((y1[i] + offset, y2[i] + offset))
    
    # 0 = 빨강(1번째), 1 = 파랑(2번째)
    color = i % 2   
    for row in range(ya, yb):
        for col in range(xa, xb):
            grid[row][col] = color


blue_area = 0
for row in range(N):
    for col in range(N):
        if(grid[row][col] == 1):
            blue_area += 1

print(blue_area)