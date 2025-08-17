n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
            
# slice 
def chk_subsequnce(a, b):
    if (b[0] in a):
        begin = a.index(b[0])
        end = begin + len(b)
        tmp_subseq = a[begin:end]
    
        if(b == tmp_subseq):
            return "Yes"
        else:
            return "No"
    else:
        return "No"


print(chk_subsequnce(a,b))
     
    
