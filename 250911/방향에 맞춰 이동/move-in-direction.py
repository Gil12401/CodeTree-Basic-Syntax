n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
# E : 0 W : 1 S : 2 N : 3 
x, y = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1] 

def move(x,y,dir,dist):
    if(dir == 'E'):
        x, y = x + dx[0]*dist, y + dy[0]*dist
    elif(dir == 'W'):
        x, y = x + dx[1]*dist, y + dy[1]*dist
    elif(dir == 'S'):
        x, y = x + dx[2]*dist, y + dy[2]*dist
    elif(dir == 'N'):
        x, y = x + dx[3]*dist, y + dy[3]*dist

    return x, y

for i in range(n):
    x, y = move(x,y,dir[i],dist[i])

print(x,y,end=" ")