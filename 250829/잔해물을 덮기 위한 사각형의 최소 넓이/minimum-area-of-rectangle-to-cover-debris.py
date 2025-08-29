x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
offset = 1000
grid = [[0 for _ in range(offset * 2 + 1)] for _ in range(offset * 2 + 1)]
x_min, y_min = x1[0] + offset, y1[0] + offset
x_max, y_max = 0, 0 

for i in range(2):
    xi_1, yi_1 = x1[i] + offset, y1[i] + offset
    xi_2, yi_2 = x2[i] + offset, y2[i] + offset

    xi_1, xi_2 = sorted((xi_1, xi_2))
    yi_1, yi_2 = sorted((yi_1, yi_2))

    for row in range(xi_1, xi_2):
        for col in range(yi_1, yi_2):
            grid[row][col] += 1
     
# x_max, y_max 구하기 
x_max, y_max = 0, 0
col_values = [grid[r][col] for r in range(len(grid))]
for row in range(x1[0]+offset,x2[0]+offset):
    if (any(grid[row])):
        x_max = row 

for c in range(len(grid[0])):
    if any(grid[r][c] for r in range(len(grid))):
        y_max = c

area = 0
for row in range(x1[0]+offset,x_max + 1):
    for col in range(y1[0]+offset,y_max + 1):
        if(grid[row][col] >= 1):
            area += 1
            
# print("x_max",x_max,"y_max",y_max)
print(area)