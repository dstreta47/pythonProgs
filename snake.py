def snake_trav(nums):
    for i in range(len(nums)):
        if i%2==0:
            for j in range(len(nums[i])):
                print(nums[i][j])
        else:
            for k in reversed(range(len(nums))):
                print(nums[i][k])            

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
snake_trav(nums)
