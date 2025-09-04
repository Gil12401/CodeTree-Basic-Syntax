N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
penalty_cnt = [0 for _ in range(N)]
student_num = -1

for i in range(len(student)):
    student_idx = student[i] - 1
    penalty_cnt[student_idx] += 1
    
    if penalty_cnt[student_idx] >= K:
        student_num = student_idx + 1
        break

print(student_num)