def mat(a):
    for i in range(len(a)):
        if i%2 ==0:
            for j in range(len(a[0])):
                print(a[i][j])
        else:
            for j in range(len(a[0])-1,-1,-1):
                print(a[i][j])        

a = [[2, 4, 6, 8, 10], 
     [3, 6, 9, 12, 15],    
     [4, 8, 12, 16, 20]]
     
mat(a)
