# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def depth(root):
            nonlocal res
            if root is None:
                return 0
            else:
                x=depth(root.left)
                y=depth(root.right)
                res=max(res,x+y+1)
                return 1+max(x,y)
        depth(root)
        return res-1
        