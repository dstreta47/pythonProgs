def lastocc(array,n,key):
    if n==0:
        return -1

    i = lastocc(array[1:],n-1,key)  
    if i == -1:
        if array[0] == key:
            return 0
        else:
            return -1

    return i+1            


array = [1,2,3,7,4,5,6,7,10]
key = 7
n = len(array)
print(lastocc(array,n,key))  

def linear_search(array,n,key):
    if n == 0:
        return -1

    if array[0]==key:
        return 0    

    i = linear_search(array[1:],n-1,key)  
    if i == -1:
        return -1

    return i+1    

#another way 
def linearSearch2(array,i,n,key):
    #base case
    if i==n:
        return -1
    #rec case    for loop like
    if array[i] == key:
        return i

    return linearSearch2(array, i+1,n,key)        

array = [1,2,3,7,4,5,6,7,10]
key = 7
n = len(array)
print(linear_search(array,n,key))  

