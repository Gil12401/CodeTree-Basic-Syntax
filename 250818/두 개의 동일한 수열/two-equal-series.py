n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
def chk_same_seq(A,B):
    sorted_A = sorted(A)
    sorted_B = sorted(B)
    if(sorted_A == sorted_B):
        return "Yes"

    return "No"

print(chk_same_seq(A,B))
