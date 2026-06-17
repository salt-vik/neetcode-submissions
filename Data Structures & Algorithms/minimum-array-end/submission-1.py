class Solution:
    def minEnd(self, n: int, x: int) -> int:
        a=bin(n-1)[2:]
        a=a[::-1]
        b=bin(x)[2:]
        b=b[::-1]
        b+=('0'*30)
        ans=[]
        i=0
        j=0
        print(a,b)
        while(j<len(a) or i<len(b)):
            print(j)
            if j==len(a):
                ans.append(int(b[i]))
            elif b[i]=='1':
                ans.append(1)
            else:
                ans.append(int(a[j]))
                j+=1
            i+=1
        count=0
        print(ans)
        for i in range(len(ans)):
            count+=ans[i]*(2**i)
        return count

