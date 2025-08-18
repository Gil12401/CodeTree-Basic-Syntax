n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
            

def chk_subsequnce(a, b):
    result = "No"
    for i in range(len(a)):
        if(a[i] == b[0]):
            begin = i
            end = min(len(a),begin + len(b))
            tmp_subseq = a[begin:end]
            if(tmp_subseq == b):
                result = "Yes"
            
    return result    
          
      

print(chk_subsequnce(a,b))

=================================================================================
[ 풀이 2. ]
def substr(start_idx):
    n, m = len(text), len(pattern)

    # 패턴이 text에 '완전히' 들어갈 수 없는 시작점이면 즉시 배제
    if start_idx + m - 1 >= n:
        return False

    # 패턴 길이 m 만큼 문자 대조
    for i in range(m):
        if text[start_idx + i] != pattern[i]:
            return False
    
    return True
     

    
