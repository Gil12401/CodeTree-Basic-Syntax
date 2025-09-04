n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
def pad_to_same_length(a, b):
    max_len = max(len(a), len(b))
    # 배열 복사 후 패딩 적용
    padded_a = list(a)
    padded_a += [padded_a[-1]] * (max_len - len(padded_a))
    
    padded_b = list(b)
    padded_b += [padded_b[-1]] * (max_len - len(padded_b))
    
    return padded_a, padded_b
    
    
a = [0]
b = [0]
a_next, b_next = 0, 0

for i in range(n):
    dx = 1
    if (d[i] == 'L'):
        dx = -1
        
    for j in range(t[i]):
        cur = a[-1] + dx
        a.append(cur)
        
for i in range(m):
    dx = 1
    if (d2[i] == 'L'):
        dx = -1
        
    cur = 0 
    for j in range(t2[i]):
        cur = b[-1] + dx
        b.append(cur)
        
padded_a, padded_b = pad_to_same_length(a,b)
# print(padded_a)
# print(padded_b)

time = 0
for t in range(len(padded_a)):
    if (t > 0 and padded_a[t] == padded_b[t]):
        time = t
        break

print(time)




    