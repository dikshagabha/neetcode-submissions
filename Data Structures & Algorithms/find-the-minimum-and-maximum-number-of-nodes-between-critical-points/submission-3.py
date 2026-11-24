# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        firstcrtical = None
        prev = head
        head = head.next
        node = 1
        res = [100000, -1]
        currentcrtical = None
        prevcrtical = None
        while head.next:
            if (head.val>prev.val and head.val>head.next.val) or (head.val<prev.val and head.val<head.next.val):
                prevcrtical = currentcrtical
                currentcrtical = node
                if firstcrtical==None:
                    firstcrtical = node
            
                if prevcrtical is not None:
                    res[0] = min(res[0], currentcrtical-prevcrtical)
                res[1] = currentcrtical-firstcrtical
            node+=1
            prev = head
            head=head.next
        if res[0]==100000:
            return [-1, -1]
        return res