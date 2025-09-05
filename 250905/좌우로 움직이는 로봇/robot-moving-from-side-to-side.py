n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
def pad_to_same_length(a, b):
    max_len = max(len(a), len(b))
    # 배열 복사 후 패딩 적용
    padded_a = list(a)
    padded_a += [padded_a[-1]] * (max_len - len(padded_a))
    
    padded_b = list(b)
    padded_b += [padded_b[-1]] * (max_len - len(padded_b))
    
    return padded_a, padded_b


def pos_after_move(_list, count, d, t):
    for i in range(count):
        dx = 1
        if (d[i] == 'L'):
            dx = -1
        for j in range(t[i]):
            cur_pos = _list[-1] + dx 
            _list.append(cur_pos)
    
    return _list


a_pos=[0]
b_pos=[0]

a_pos = pos_after_move(a_pos, n, d, t)
b_pos = pos_after_move(b_pos, m, d_b, t_b)
a_pos, b_pos = pad_to_same_length(a_pos, b_pos)

count = 0
for i in range(1, len(a_pos)):
    if(a_pos[i] == b_pos[i] and a_pos[i-1] != b_pos[i-1]):
        count += 1
    
print(count)