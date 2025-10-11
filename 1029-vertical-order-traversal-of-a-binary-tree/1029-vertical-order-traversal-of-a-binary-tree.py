# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        nodes=[]
        def dfs(node,x,y):
            if node:
                nodes.append((x,y,node.val))
                dfs(node.left,x-1,y+1)
                dfs(node.right,x+1,y+1)
        dfs(root,0,0)
        nodes.sort()
        ans=defaultdict(list)
        for x,y,val in nodes:
            ans[x].append(val)
        return [ans[x] for x in sorted(ans)]        