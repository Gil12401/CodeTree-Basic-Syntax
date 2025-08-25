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
cur = offset  
next_cur = 0
prev_dx = moves[0]
for dx in moves:
    if(prev_dx * dx < 0):
        cur = next_cur
        
    next_cur = cur + dx
    
    # print("prev_dx : ",prev_dx,"dx : ",dx)
   #  print("dx : ",dx,"cur :",cur,"next_cur :",next_cur)
    
    # 현재 위치 → 다음 위치까지 지나간 구간 체크
    for j in range(min(cur, next_cur), max(cur, next_cur)):
        if 0 <= j < len(x_points):
            if(len(x_points[j]) == 3 or x_points[j] == "G"):
                x_points[j] = "G"
            elif(cur < next_cur):
                x_points[j] += "B"
            elif(cur > next_cur):
                x_points[j] += "W"
    
    if(abs(dx) > 1): 
        cur = next_cur
    
    prev_dx = dx
       

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