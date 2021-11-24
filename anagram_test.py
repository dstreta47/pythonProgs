def anagram_test(s1,s2):
    char = [0] * 256
    
    for i in range(len(s1)):
        # if char[ord(s1[i])] == -1:
        #     char[ord(s1[i])] = 1
        # else:
        print("comparing",s1[i],s2[i])
        char[ord(s1[i])] +=1
        char[ord(s2[i])] -=1


    # for j in range(len(s2)):
    #     if char[ord(s2[j])] == -1:
    #         char[ord(s2[j])] = 1
    #     else:
    #         char[ord(s2[j])] -=1      

    return char                


s1 = "GEEKSFORGEEKS"
s2 = "GEEKSFOGNEKSR"
char = anagram_test(s1,s2)
for i,j in enumerate(char):
    if j>0:
        print(chr(i),j)

