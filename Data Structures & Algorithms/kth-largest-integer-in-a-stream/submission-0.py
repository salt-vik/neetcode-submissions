from heapq import *
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.x = []
        for i in nums:
            if len(self.x) < k:
                heappush(self.x, i)
            else:
                if i > self.x[0]:
                    heappushpop(self.x, i)
    def add(self, val: int) -> int:
        if len(self.x) < self.k:
            heappush(self.x, val)
        elif val > self.x[0]:
            heappushpop(self.x, val)
            
        return self.x[0]