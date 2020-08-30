x = -123

def reverse(x):
    if x > 2**31-1 or x < -2**31:
        return 0

    else:
        qn = str(x)
        if x >=0:
            ans = qn[::-1]
        
        else:
            temp = qn[1:]
            ans = "-" + temp[::-1]
            
    if int(ans) > 2**31-1 or int(ans) < -2**31:
        return 0
    else:
        return ans
    
print(reverse(123))
