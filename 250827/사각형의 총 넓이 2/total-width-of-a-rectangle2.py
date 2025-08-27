n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a+100)
    y1.append(b+100)
    x2.append(c+100)
    y2.append(d+100)

# Please write your code here.
grid = [[0 for _ in range(201)] for _ in range(201)]

for i in range(n):
    xa, xb = sorted((x1[i], x2[i]))
    ya, yb = sorted((y1[i], y2[i]))
    for row in range(xa, xb):
        for col in range(ya, yb):
            grid[row][col] = 1


width = 0
for row in range(201):
    for col in range(201):
        if(grid[row][col] >= 1):
            width += 1

print(width)