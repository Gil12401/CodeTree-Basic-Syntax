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
     
    