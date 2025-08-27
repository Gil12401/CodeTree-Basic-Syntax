n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# points = [(1,2), (3,4), (5,6)]
# x = [1, 3, 5]
# y = [2, 4, 6]

# Please write your code here.
# 1. 전체 사각형 만들기 ( Offset 고려 )
offset = 100
grid = [[0 for _ in range(offset*2 + 1)] for _ in range(offset*2 + 1)]

# 2. 각 사각형의 넓이 합하기 (겹친 부분은 제외)
for i in range(n):
    xi, yi = int(x[i]), int(y[i])
    xi += offset
    yi += offset

    for row in range(xi,xi+8):
        for col in range(yi,yi+8):
            grid[row][col] = 1

area = 0
for row in range(offset*2 + 1):
    for col in range(offset*2 + 1):
        if(grid[row][col] >= 1):
            area += 1

print(area)


    

    

