# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow, fast = head, head.next
        while fast:
            node = ListNode(math.gcd(slow.val, fast.val), fast)
            slow.next = node 
            slow = fast
            fast = fast.next
        return head
        