# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itter = head
        total = 0
        while itter:
            total+=1
            itter = itter.next
        
        cur_val = total-n
        if cur_val==0:
            return head.next
        
        itter = head
        prev=ListNode(0)
        while cur_val:
            cur_val-=1
            prev=itter
            itter = itter.next
        temp=itter.next 
        prev.next=temp
        return head