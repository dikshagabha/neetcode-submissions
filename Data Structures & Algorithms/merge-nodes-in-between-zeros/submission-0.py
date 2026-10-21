# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = res = ListNode()
        cs = 0
        while head:
            if head.val==0:
                res.next = ListNode(cs)
                res= res.next
                cs = 0
            cs+=head.val
            head=head.next
            

        return r.next.next