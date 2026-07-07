class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for j in nums:
            arr=[]
            for k in ans:
                f=k.copy()
                f.append(j)
                arr.append(f)
            ans+=arr
        return ans
        