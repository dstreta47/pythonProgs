class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(a,l, r):
            if l==r:
                output.append(a[:])
            else:
                for i in range(l,r+1):
                    a[l], a[i] = a[i], a[l]
                    backtrack(a, l+1, r)
                    a[l], a[i] = a[i], a[l]         
        
        n = len(nums)
        output = []
        a= backtrack(nums,0, n-1)
        return output    
        
