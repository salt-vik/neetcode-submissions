class Solution:
    def getSum(self, a: int, b: int) -> int:
        return 2*(a&b)+(a^b)
        