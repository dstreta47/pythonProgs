# from collections import Counter
# #using hash table
# def string_frq(string1):
#     dict1 = {}
#     for i in string1:
#         if i not in dict1:
#             dict1[i] = 1

#         else:
#             dict1[i]+=1    

#     return dict1        


# #using counter
# test = "geeksforgeeks"
# # print(string_frq(test))  
# test1 = Counter(test)

# print(test1)

#using ord
def freq_counter(test):
    char = [-1]*256
    s=ord('a')

    for i in range(len(test)):
        if char[ord(test[i])-ord('a')] == -1:
            char[ord(test[i])-ord('a')] =1
        else:
            char[ord(test[i])-ord('a')]  +=1 

    return char        

test = "geeksforgeeks"
res = freq_counter(test)
for i,j in enumerate(res):
    if j !=-1:
        print(chr(i+97),j)
