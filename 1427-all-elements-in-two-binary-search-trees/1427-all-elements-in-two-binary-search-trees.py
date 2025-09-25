class Solution:
    def getAllElements(self, root1: TreeNode, root2:TreeNode) -> List[int]:
        def pushLeft(stack,node):
            while node:
                stack.append(node)
                node=node.left
        stack1,stack2,res=[],[],[]
        pushLeft(stack1,root1)
        pushLeft(stack2,root2)
        while stack1 or stack2:
            if not stack2 or (stack1 and stack1[-1].val<=stack2[-1].val):
                node=stack1.pop()
                res.append(node.val)
                pushLeft(stack1,node.right)
            else:
                node=stack2.pop()
                res.append(node.val)
                pushLeft(stack2,node.right)
        return res
        