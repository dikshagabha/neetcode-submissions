# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def cursum_path(root, cursum):
            if root==None:
                return False
            if root.left==None and root.right==None:
                return cursum+root.val == targetSum
            
            return cursum_path(root.left, cursum+root.val) or cursum_path(root.right,cursum+root.val)

        return cursum_path(root, 0)