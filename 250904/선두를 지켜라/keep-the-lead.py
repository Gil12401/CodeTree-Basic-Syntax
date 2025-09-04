n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
a = [0]
b = [0]

def get_list_after_movement(list, length, v, t):
    _list = list
    
    for i in range(length):
        for j in range(t[i]):
            cur = _list[-1] + v[i]
            _list.append(cur)

    return _list

a = get_list_after_movement(a, n, v, t)
b = get_list_after_movement(b, m, v2, t2)

first_per_time = ['E'] 

for i in range(1,len(a)):
    if a[i] > b[i]:
        first_per_time.append('A')
    elif a[i] < b[i]:
        first_per_time.append('B')
    else:
        prev_1st = first_per_time[-1]
        first_per_time.append(prev_1st)

# 1. 'E' 제거
first_per_time = [x for x in first_per_time if x != 'E']

# ['B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
# 2. 연속 중복 제거
compressed = [first_per_time[0]]  # 첫 원소는 무조건 넣음
for x in first_per_time[1:]:
    if x != compressed[-1]:
        compressed.append(x)

# print(a)
# print(b)
# print(first_per_time)
# print(compressed)
print(len(compressed)-1)