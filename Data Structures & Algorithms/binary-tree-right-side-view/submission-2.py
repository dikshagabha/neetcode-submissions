# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        res = []
        q = [[root]]
        res = [root.val]
        while q:
            cur = q.pop()
            temp = []
            for i in cur:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if len(temp)>=1:
                res.append(temp[-1].val)
                q.append(temp)
        return res

