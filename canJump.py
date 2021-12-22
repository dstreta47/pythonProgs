# def canJump(nums):
#     goal = len(nums)-1

#     for i in range(len(nums)-1,-1,-1):
#         if i+nums[i]>=goal:
#             goal = i
#         return True if goal ==0 else False    

def canJump(nums):
        lastPos = len(nums) - 1
        for i in range(len(nums)- 1,-1,-1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0 


nums = [2,3,1,1,4]
print(canJump(nums))

