class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        for i in nums:
            pre.append(pre[-1]*i)
        nums=nums[::-1]
        suff=[1]
        for i in nums:
            suff.append(suff[-1]*i)
        pre.pop()
        suff.pop()
        ans=[]
        for i in range(len(nums)):
            ans.append(pre[i]*suff[len(suff)-i-1])
        return ans