def staircaseSearch(a,n,m,key):
    i=0
    j=m-1
    iskeypresent = False
    while(i<n and j>=0):
        if a[i][j]==key:
            print("key found at index")
            print("row",i,"column",j)
            iskeypresent  = True
            break
        elif(a[i][j]<key):
            i+=1
        else:
            j-=1
    if iskeypresent == False:
        print("key is not found")
a = [[1, 2, 3, 4], 
     [5, 6, 7, 8],    
     [9, 10, 11, 12],
     [13,14,15,16]]
n = len(a)
m=len(a[0])
key =14
staircaseSearch(a,n,m,key)
