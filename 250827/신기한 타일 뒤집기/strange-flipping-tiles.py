n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

# 0 ~ 2*MAX_K
# 원점 : cur = MAX_K
MAX_K = 100000 
cur = MAX_K

colors = [0] * (2 * MAX_K + 1)
b, w = 0, 0

# n개의 이동 명령 
# x L,R : x칸 칠하기 / (x-1)번 이동 
for i in range(n):
    x, dir = commands[i]
    x = int(x)
    
    # Left 
    if (dir == 'L'):
        while (x > 0):
            colors[cur] = 'W'
            x -= 1 

            if (x >= 1):
                cur -= 1 
            
            
    else: 
        while (x > 0):
            colors[cur] = 'B'
            x -= 1
        
            if (x >= 1):
                cur += 1


w = colors.count('W')
b = colors.count('B')

print(w,b,end=" ")