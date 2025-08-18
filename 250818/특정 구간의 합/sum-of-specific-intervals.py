n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def get_sum_from_query(q):
    _sum = 0
    start = q[0] - 1
    end = q[1]
        
    for i in range(start, end):
        _sum += arr[i]
    
    return _sum
    
for q in queries:
    print(get_sum_from_query(q))
        
