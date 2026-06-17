class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        hi=x
        while(low<=hi):
            mid=(low+hi)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                hi=mid-1
            else:
                low=mid+1
        return hi
        