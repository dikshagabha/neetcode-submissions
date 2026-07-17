"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        l = []


        def traverse(root):
            if root==None:
                return
            
            for i in root.children:
                traverse(i)
                #l.append(i.val)
                
            l.append(root.val)
        

        traverse(root)
        return l