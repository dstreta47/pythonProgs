def even_dig(nums):
    res = 0
    for i in nums:
        cnt = 0
        while(i>0):
            i = i//10
            cnt+=1
        if cnt % 2 ==0:
            res +=1  
    return res    


# nums = [12,345,2,6,7896]
nums = [555,901,482,1771]
print(even_dig(nums))
