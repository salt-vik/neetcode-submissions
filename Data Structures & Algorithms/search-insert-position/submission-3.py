class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        hi = len(nums) - 1
        
        while low <= hi:
            mid = (low + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                hi = mid - 1
        return low