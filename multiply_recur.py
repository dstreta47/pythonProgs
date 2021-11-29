def multiply_recur(a,n):
    if n == 0:
        return 0

    return a + multiply_recur(a,n-1)    


print(multiply_recur(2,3))    
