class Solution:
    def sortedListToBST(self,head:ListNode)->TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        prev=None
        slow=head
        fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev:
            prev.next=None
        root=TreeNode(slow.val)
        root.left=self.sortedListToBST(head if slow != head else None)
        root.right=self.sortedListToBST(slow.next)
        return root