class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        seen={}
        for i in strs:
            k=''.join(sorted(i))
            if k in seen:
                ans[seen[k]].append(i)
            else:
                ans.append([i])
                seen[k]=len(ans)-1
        return ans
        