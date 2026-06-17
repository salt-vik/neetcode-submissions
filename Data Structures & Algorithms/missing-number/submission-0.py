class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=sum(nums)
        return (len(nums)*(len(nums)+1))//2-x
        