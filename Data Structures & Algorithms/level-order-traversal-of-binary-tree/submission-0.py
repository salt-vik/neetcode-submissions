# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        x=[root]
        y=[]
        if root==None:
            return []
        while(x):
            ans.append([])
            for j in x:
                ans[-1].append(j.val)
                if j.right is not None:
                    y.append(j.right)
                if j.left is not None:
                    y.append(j.left)
            x=y
            y=[]
            ans[-1]=ans[-1][::-1]
        return ans
            

        