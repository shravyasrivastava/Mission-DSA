class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        left=self.rangeSumBST(root.left,low,high)
        right=self.rangeSumBST(root.right,low,high)
        if low<=root.val<=high:
            c=root.val
        else:
            c=0
        return c+left+right

        