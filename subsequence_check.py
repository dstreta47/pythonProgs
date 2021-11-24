
def subsequence(s1,s2):
    j=0
    for i in range(len(s1)):
        if s1[i] == s2[j]:
            i+=1
            j+=1
        else:
            i+=1

        if(j==len(s2)):
            print("the sequence is present")



s1 = "GEEKSFORGEEKS"
s2 = "GRGEff"
print(subsequence(s1,s2))

