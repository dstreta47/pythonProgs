def subsequence(string1, string2,n,m):
    j =0
    i=0
    while(i<n and j<m):
        print(string1[i],string2[j])
        if string1[i] == string2[j]:
            j+=1
        i+=1 
    return j==m       



print(subsequence('ABCDEF','AfDE',6,3))            



