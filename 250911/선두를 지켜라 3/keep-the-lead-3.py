N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
a = [0]
b = [0]
first_board = [] 

def get_list_after_movement(list, length, v, t):
    _list = list
    
    for i in range(length):
        for j in range(t[i]):
            cur = _list[-1] + v[i]
            _list.append(cur)

    return _list

a = get_list_after_movement(a, N, v, t)
b = get_list_after_movement(b, M, v2, t2)

# A와 B 중 더 앞서 있는 경우를 확인합니다.
# 1등 -> A : 1, B : 2, (AB)공동 : 3 
leader, cur_leader = 0, 0
count = 0
for i in range(1, len(a)):
    if a[i] > b[i]:
        leader = 1
    
    elif a[i] < b[i]:
        leader = 2
    
    elif a[i] == b[i]:
        leader = 3 
    
    if (cur_leader != leader):
        count += 1 
    
    cur_leader = leader

print(count)



