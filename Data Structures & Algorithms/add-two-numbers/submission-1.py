# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = res = ListNode(0)
        def remain(l, carry):
            while l:
                cs = l.val+carry
                if cs>=10:
                    carry = cs//10
                    cs = cs%10
                else:
                    carry = 0
                nonlocal res
                res.next = ListNode(cs)
                res=res.next
                l = l.next
            return carry

        carry = 0
        cs = 0
        while l1 and l2:
            cs = l1.val+l2.val+carry
            if cs>=10:
                carry = cs//10
                cs = cs%10
                
            else:
                carry = 0
            
            res.next = ListNode(cs)
            res=res.next
            l1 = l1.next
            l2 = l2.next
       
        carry = remain(l1, carry)
        carry = remain(l2, carry)
        # if carry:
        #     return  ListNode(carry, l.next)
        if carry:
            res.next = ListNode(carry)
        return l.next