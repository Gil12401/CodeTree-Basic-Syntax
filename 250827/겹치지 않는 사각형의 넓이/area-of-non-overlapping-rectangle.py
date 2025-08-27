x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split()) # A 
x1[1], y1[1], x2[1], y2[1] = map(int, input().split()) # B 
x1[2], y1[2], x2[2], y2[2] = map(int, input().split()) # M 

# Please write your code here.
grid = [[0 for _ in range(2001)] for _ in range(2001)]

for i in range(2):
    xa, xb = sorted((x1[i], x2[i]))
    xa, xb = xa + 1000, xb + 1000

    ya, yb = sorted((y1[i], y2[i]))
    ya, yb = ya + 1000, yb + 1000

    for row in range(xa, xb):
        for col in range(ya, yb):
            grid[row][col] = 1

# M 
mx_a, mx_b = sorted((x1[2], x2[2]))
mx_a, mx_b = mx_a + 1000, mx_b + 1000

my_a, my_b = sorted((y1[2], y2[2]))
my_a, my_b = my_a + 1000, my_b + 1000

for row in range(mx_a, mx_b):
    for col in range(my_a, my_b):
        if(grid[row][col] >= 1):
            grid[row][col] = 0


area = 0
for row in range(2001):
    for col in range(2001):
        if(grid[row][col] >= 1):
            area += 1

print(area)