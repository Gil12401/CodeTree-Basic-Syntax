dirs = input()

# Please write your code here.
# 90 degrees rotate : N -> E -> S -> W 
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0] 
x, y = 0, 0


def action(x,y,dir):
    global cur_dir
    if(dir == 'R'):
        cur_dir = (cur_dir + 1) % 4
    elif(dir == 'L'):
        cur_dir = (cur_dir - 1 + 4) % 4

    if(dir == 'F'):
        x, y = x + dx[cur_dir], y + dy[cur_dir]
    
    return x, y

cur_dir = 0
for dir in dirs:
    x, y = action(x,y,dir)

print(x,y,end=" ")