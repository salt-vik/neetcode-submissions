class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        prices=prices[::-1]
        maximum=[prices[0]]
        for i in prices[1:]:
            maximum.append(max(maximum[-1],i))
        maximum=maximum[::-1]
        prices=prices[::-1]
        ans=[]
        for j in range(len(prices)-1):
            ans.append(maximum[j+1]-prices[j])
        return max(max(ans),0)