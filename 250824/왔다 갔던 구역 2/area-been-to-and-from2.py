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