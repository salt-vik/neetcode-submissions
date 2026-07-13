class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = nums[0]
        cur_min, cur_max = 1, 1
    
        for n in nums:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
                
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)
            
            res = max(res, cur_max)
            
        return res