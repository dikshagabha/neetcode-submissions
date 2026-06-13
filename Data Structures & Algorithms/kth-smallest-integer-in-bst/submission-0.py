# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if root == None or k<0:
        #     return -1
        
        res = []
        def itter(node, pos):
            if node==None:
                return
            
            if node.left:
                itter(node.left, pos)
                
            
            res.append(node.val)
            if len(res)==k:
                return
            if node.right:
                itter(node.right, pos+2)

        itter(root, 0)
        #print(res)
        return res[k-1]
        # if root.left:
        #     return self.kthSmallest(root.left, k)
        # if k-1==0:
        #     return root.val
        # if root.right:
        #     return self.kthSmallest(root.right, k-2)