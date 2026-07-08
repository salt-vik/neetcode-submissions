class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=max(nums)
        pre=0
        nums.append(float('-inf'))
        for i in nums:
            pre+=i
            ans=max(ans,pre)
            if pre<0:
                pre=0
            print(pre,ans)
        return ans