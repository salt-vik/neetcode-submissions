# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        x,y=min(p.val,q.val),max(p.val,q.val)
        while(True):
            if root.val> x and root.val>y:
                root=root.left
            if root.val>x and root.val<y:
                return root
            if root.val<x and root.val<y:
                root=root.right
            if root.val==x or root.val==y:
                return root
                
        