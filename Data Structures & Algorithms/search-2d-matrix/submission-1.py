class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        v=len(matrix)
        x=len(matrix[0])
        low=0
        hi=v-1
        while(low<=hi):
            mid=(low+hi)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                low=mid+1
            else:
                hi=mid-1
        check=hi
        low=0
        hi=x-1
        print(check)
        while(low<=hi):
            mid=(low+hi)//2
            if matrix[check][mid]==target:
                return True
            elif matrix[check][mid]<target:
                low=mid+1
            else:
                hi=mid-1
        return False


        