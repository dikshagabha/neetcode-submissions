# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        get_root = {root.val:(None, 0)}
        
        def fill_Roots(node, l):
            if node.left:
                get_root[node.left.val] = (node, l)
                fill_Roots(node.left, l+1)
            if node.right:
                get_root[node.right.val] = (node, l)
                fill_Roots(node.right, l+1)
        fill_Roots(root, 1)

        rootp, levelp = get_root[p.val]
        rootq, levelq = get_root[q.val]
        while levelp>levelq:
            p=rootp
            rootp, levelp = get_root[p.val]
        
        while levelq>levelp:
            q=rootq
            rootq, levelq = get_root[q.val]
        
        while p != q and p!=None and q!=None:
            q, levelq = get_root[q.val]
            p, levelp = get_root[p.val]
        return p
