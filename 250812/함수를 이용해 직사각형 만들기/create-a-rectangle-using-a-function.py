row, col = map(int, input().split())

# Please write your code here.
def write_rect_n_m(row, col):
    for _ in range(row):
        print("1" * col)

write_rect_n_m(row,col)