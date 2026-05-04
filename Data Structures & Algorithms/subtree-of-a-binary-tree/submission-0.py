# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if not self.func(root, subRoot):
            if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
                return True
            else: 
                return False
        else:
            return True
        
    def func(self, p, q)->bool:
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return self.func(p.left, q.left) and self.func(p.right, q.right)
