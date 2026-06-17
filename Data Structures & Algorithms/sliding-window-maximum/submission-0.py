from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        stack1 = [] 
        stack2 = [] 
        
        def push(val):
            current_max = val if not stack1 else max(val, stack1[-1][1])
            stack1.append([val, current_max])
            
        def pop():
            if not stack2:
                while stack1:
                    val, _ = stack1.pop()
                    current_max = val if not stack2 else max(val, stack2[-1][1])
                    stack2.append([val, current_max])
            return stack2.pop()
            
        def get_max():
            if not stack1 and not stack2:
                return float('-inf')
            if not stack1:
                return stack2[-1][1]
            if not stack2:
                return stack1[-1][1]
            return max(stack1[-1][1], stack2[-1][1])

        result = []
        
        for i in range(k):
            push(nums[i])
        result.append(get_max())
        for i in range(k, len(nums)):
            pop()          
            push(nums[i])   
            result.append(get_max()) 
            
        return result