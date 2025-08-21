n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x_points = [0 for _ in range(100)]
offset = -1 

def draw_segment(segment):
    x1, x2 = segment
    x1 += offset 
    x2 += offset

    for i in range(x1,x2+1):
        x_points[i] += 1 

for segment in segments:
    draw_segment(segment)

sorted_x_points=sorted(x_points)
print(sorted_x_points[-1])


