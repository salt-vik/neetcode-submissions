class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        if len(s1)>len(s2):
            return False
        dic={}
        for i in s1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        dic1={}
        L=0
        R=0
        while(R<k):
            if s2[R] in dic1:
                dic1[s2[R]]+=1
            else:
                dic1[s2[R]]=1
            R+=1
        if dic==dic1:
            return True
        while(R<len(s2)):
            if s2[R] in dic1:
                dic1[s2[R]]+=1
            else:
                dic1[s2[R]]=1
            if s2[L] in dic1:
                dic1[s2[L]]-=1
                if dic1[s2[L]]==0:
                    dic1.pop(s2[L])
            if dic1==dic:
                return True
            L+=1
            R+=1
        return False
                


            


        
        