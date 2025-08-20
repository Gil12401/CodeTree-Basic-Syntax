MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Grade:
    def __init__(self, codename="", score=0):
        self.codename = codename
        self.score = score 

Grades = [Grade(codenames[i], scores[i]) for i in range(MAX_N)]
sorted_Grades = sorted(Grades, key=lambda g: g.score)
print(sorted_Grades[0].codename,sorted_Grades[0].score)


