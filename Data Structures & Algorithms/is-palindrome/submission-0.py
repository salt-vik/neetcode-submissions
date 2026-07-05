class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=[]
        for i in s.lower():
            if i.isalnum()==True:
                ans.append(i)
        return ans==ans[::-1]
        