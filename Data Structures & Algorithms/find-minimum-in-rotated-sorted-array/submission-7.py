class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        hi=len(nums)-1
        while(low<=hi):
            mid=(low+hi)//2
            print(mid)
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]<nums[0]:
                hi=mid-1
            else:
                low=mid+1
        return nums[0]

        