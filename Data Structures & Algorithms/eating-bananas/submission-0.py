class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo=1
        hi=int(1e9)
        ans=-1
        while(lo<=hi):
            mid=(lo+hi)//2
            if sum([(i+mid-1)//mid for i in piles])<=h:
                hi=mid-1
                ans=mid
            else:
                lo=mid+1
        return ans
            
        