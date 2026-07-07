# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans=[]
        def dfs(root):
            if root is None:
                ans.append(None)
            else:
                dfs(root.left)
                dfs(root.right)
                ans.append(root.val)
        dfs(p)
        dfs(q)
        print(ans[:len(ans)//2])
        print(ans[len(ans)//2:])
        return ans[:len(ans)//2]==ans[len(ans)//2:]
        