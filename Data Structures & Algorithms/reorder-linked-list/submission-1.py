# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        
        cur = head
        while cur and cur.next and cur.next.next:
            last_node = cur
            while last_node.next and last_node.next.next:
                last_node = last_node.next
        
            tail = cur.next
            cur.next = last_node.next
            
            cur.next.next = tail
            last_node.next = None
            cur = cur.next.next



            

