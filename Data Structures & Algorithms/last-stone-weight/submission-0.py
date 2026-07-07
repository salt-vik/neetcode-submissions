from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-1*i for i in stones ]
        heapify(stones)
        while(len(stones)>1):
            x=heappop(stones)
            y=heappop(stones)
            if x==y:
                continue
            else:
                heappush(stones,-1*(y-x))
        if stones==[]:
            return 0
        else:
            return -1*stones[0]
        