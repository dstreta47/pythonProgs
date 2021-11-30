def stringtoInt(a,n):
    if n==0:
        return 0

    digit = int(a[n-1])
    rem = stringtoInt(a,n-1)

    return rem *10 + digit


a = "1234"
n = len(a)
print(stringtoInt(a,n)+1) 
