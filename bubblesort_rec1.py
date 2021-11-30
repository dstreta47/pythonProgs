def bubblesort(array,j,n):
    if n == 1:
        return

    if j == n-1:
        return bubblesort(array,0,n-1)

    if array[j]>array[j+1]:
        array[j],array[j+1] = array[j+1], array[j]

    bubblesort(array, j+1,n)
    return     


array = [5,4,3,1,2]
n=5
print(bubblesort(array,0,5))
