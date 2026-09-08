# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node,parent,depth):
            if not node:
                return
            if node.val==x:
                info[x]=(parent,depth)
            if node.val==y:
                info[y]=(parent,depth)
            dfs(node.left,node,depth+1)
            dfs(node.right,node,depth+1)
        info={}
        dfs(root,None,0)
        parent_x,depth_x=info[x]
        parent_y,depth_y=info[y]
        return depth_x==depth_y and parent_x!=parent_y
        