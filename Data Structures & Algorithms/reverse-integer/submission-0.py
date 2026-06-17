class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            s=int(((str(x))[::-1])[:-1])
            s=s*-1
        else:
            s=int((str(x))[::-1])
        print(s)
        if s>=2**31 or (-1*s)>2**31:
            return 0
        else:
            return s