def issorted(array):
    n = len(array)
    if n==0 or n==1:
        return True

    if array[0]<array[1] and issorted(array[1:]):
        return True

    return False        


issorted([1,2,3,14,15])    
