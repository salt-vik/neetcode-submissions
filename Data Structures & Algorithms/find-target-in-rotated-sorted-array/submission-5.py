from bisect import bisect_left
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low, hi = 0, len(nums) - 1
        while low < hi:
            mid = (low + hi) // 2
            if nums[mid] > nums[hi]:
                low = mid + 1
            else:
                hi = mid
        pivot = low
        if target >= nums[pivot] and target <= nums[-1]:
            k = bisect_left(nums, target, lo=pivot, hi=len(nums))
        else:
            k = bisect_left(nums, target, lo=0, hi=pivot)
        if k < len(nums) and nums[k] == target:
            return k
        return -1