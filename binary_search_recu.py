def binary_search_non_Recursive(array,element):
    n = len(array)
    i=0
    while(i<n):
        mid = n//2
        if array[mid] == element:
            return mid 
        elif array[mid]<element:
            i = mid+1
        else:
            i= mid-1       


def binary_search(array,l,r,element):
    if r>=1:
        mid = 1+(r-l)//2

        if array[mid]==element:
            return mid

        elif array[mid]>element:
            return binary_search(array,l,mid-1,element)
        else:
            return binary_search(array,mid+1,r,element)   
    else:
        return -1          


array = [1,2,3,4]
print(binary_search(array,0,len(array),3))
print(binary_search_non_Recursive(array,3))
