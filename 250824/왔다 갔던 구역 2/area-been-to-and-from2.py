n = int(input())
x = []
dir = [] 
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here
next_dxs = [] 
x_points = [] 
x_start, offset, x_points_len = 0, 0, 0

def set_next_dxs(next_dxs):
    for i in range(n):
        next_dx = x[i]
        if (dir[i] == "L"):
            next_dx = -x[i]

        next_dxs.append(next_dx)
    

def set_x_points():
    global x_points, x_start, x_points_len
    
    # TO DO 1. min / max x_location 
    x_locations = []
    x_location = 0

    for next_dx in next_dxs:
        x_location += next_dx
        x_locations.append(x_location)
    
    sorted_x_locations = sorted(x_locations)

    sorted_x_min = sorted_x_locations[0]
    sorted_x_max = sorted_x_locations[-1]

    x_points_len = sorted_x_max 

    if(sorted_x_min < 0):
        x_start = -sorted_x_min
        x_points_len = sorted_x_max - sorted_x_min        


    # init x_points 
    x_points = [0 for _ in range(x_points_len+1)]


def move_x(next_dxs):
    global x_points, x_start, x_points_len
    cur_x = x_start

    for i in range(n):   
        next_x = cur_x + next_dxs[i] 
        # print("move range:(",min(cur_x, next_x),",",max(cur_x, next_x),")")

        for j in range(min(cur_x, next_x),max(cur_x, next_x)):
            if 0 <= j < len(x_points):
                x_points[j] += 1
        
        cur_x = next_x


set_next_dxs(next_dxs)
set_x_points()
move_x(next_dxs)

count = 0
for x_range in x_points:
    if(x_range >= 2):
        count += 1

# print(x_points)

print(count)

################################################################

# 명령 개수 입력
n = int(input())

# 방향까지 반영한 이동 거리 배열
moves = []
for _ in range(n):
    xi, di = input().split()
    xi = int(xi)
    # 오른쪽이면 +, 왼쪽이면 -로 변환
    moves.append(xi if di == "R" else -xi)

# =========================
# 1. 모든 이동을 따라가며 좌표 기록
# =========================
locations = [0]       # 출발점은 항상 0
cur = 0
for dx in moves:
    cur += dx
    locations.append(cur)

# =========================
# 2. 좌표 범위(min, max) 구하기
# =========================
x_min, x_max = min(locations), max(locations)

# 음수 좌표도 쓸 수 있게 offset 적용
offset = -x_min

# 전체 경로 범위 크기만큼 리스트 준비
x_points = [0] * (x_max - x_min + 1)

# =========================
# 3. 실제로 이동하면서 '지나간 구간' 카운트
# =========================
cur = offset  # 시작 위치 보정
for dx in moves:
    next_cur = cur + dx
    # 현재 위치 → 다음 위치까지 지나간 구간 체크
    for j in range(min(cur, next_cur), max(cur, next_cur)):
        x_points[j] += 1
    cur = next_cur

# =========================
# 4. 2번 이상 지난 영역의 크기 세기
# =========================
count = sum(1 for v in x_points if v >= 2)
print(count)
