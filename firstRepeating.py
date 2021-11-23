def firstRepeating(str):
    char1 = [-1] *256
    res = 9999

    for i in range(len(str)):
        if char1[ord(str[i])] == -1:
            char1[ord(str[i])]=i
        else:
            res = min(res,char1[ord(str[i])])

    return str[res]


str = "anccb"
index = firstRepeating(str)  
print(index)  
