n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
moves = []
for i in range(n):
    xi, di = commands[i]
    xi = int(xi)
    moves.append(xi if di == "R" else -xi)

# 1. 모든 이동을 따라가며 좌표 기록
locations = [0]       
cur = 0
for dx in moves:
    cur += dx
    locations.append(cur)

# 2. 좌표 범위(min, max), 전체 경로 범위 크기 구하기
x_min, x_max = min(locations), max(locations)
offset = -x_min
x_points = [""] * (x_max - x_min + 1)

# 3. 실제로 이동하면서 '지나간 구간' 카운트
cur = 0 
if(offset < 0):
    cur = offset  
    
for dx in moves:
    # (타일 위에 서 있음) = (구간의 시작점에 서 있음) 
    move_count = abs(dx)
    unit_dx = move_count // dx 
    
    # x L : x개의 칸 칠하기, (x-1)회 이동 
    for i in range(move_count):
        if(len(x_points[cur]) == 3 or x_points[cur] == "G"):
            x_points[cur] = "G"
        elif(unit_dx > 0):
            x_points[cur] += "B"
        elif(unit_dx < 0):
            x_points[cur] += "W"
    
        if (i > 0):
            cur += unit_dx
    
           
# W, B, G 순으로 갯수 출력 
w_count, b_count, g_count = 0, 0, 0
for color in x_points:
    last_color = ""
    if(len(color) > 0):
        last_color = color[-1]  

    if(last_color == "W"):
        w_count += 1
    elif(last_color == "B"):
        b_count += 1
    elif(last_color == "G"):
        g_count += 1
 
# print(tiles_color)
# print(x_points)
print(w_count,b_count,g_count,end=" ")