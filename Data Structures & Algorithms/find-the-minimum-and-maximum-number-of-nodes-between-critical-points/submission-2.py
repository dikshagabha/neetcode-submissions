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
        mincri, maxcri = 100000, -1
        currentcrtical = None
        prevcrtical = None
        while head.next:
            if (head.val>prev.val and head.val>head.next.val) or (head.val<prev.val and head.val<head.next.val):
                prevcrtical = currentcrtical
                currentcrtical = node
                #print(firstcrtical, prevcrtical, currentcrtical, head.val)
                if firstcrtical==None:
                    firstcrtical = node
            
                if prevcrtical is not None:
                    mincri = min(mincri, currentcrtical-prevcrtical)
                maxcri = currentcrtical-firstcrtical
            node+=1
            prev = head
            head=head.next
        if mincri==100000:
            return [-1, -1]
        return [mincri, maxcri]