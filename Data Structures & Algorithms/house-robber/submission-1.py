class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[1],nums[0])
        dp0=0
        dp1=nums[0]
        dp2=nums[1]
        for i in range(2,len(nums)):
            temp=nums[i]+max(dp0,dp1)
            dp0,dp1,dp2=dp1,dp2,temp
        return max(dp1,dp2)
        


        