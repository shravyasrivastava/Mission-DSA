class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans=-math.inf
        def maxPathSumDownFrom(root:TreeNode | None)->int:
            nonlocal ans
            if not root:
                return 0
            l=max(0,maxPathSumDownFrom(root.left))
            r=max(0,maxPathSumDownFrom(root.right))
            ans=max(ans,root.val+l+r)
            return root.val+max(l,r)
        maxPathSumDownFrom(root)
        return ans

        