class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        k=0
        ans=[0]*(len(temperatures))
        for i in temperatures:
            while( stack and i>stack[-1][0]):
                x=stack.pop()
                ans[x[1]]=(k-x[1])
            stack.append([i,k])
            k+=1
        return ans