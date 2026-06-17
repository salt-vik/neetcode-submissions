class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi=len(nums)-1
        low=0
        ans=-1
        while(low<=hi):
            mid=(low+hi)//2
            if nums[mid]==target:
                ans=mid
                break
            elif nums[mid]<target:
                low=mid+1
            else:
                hi=mid-1
        return ans
            
        