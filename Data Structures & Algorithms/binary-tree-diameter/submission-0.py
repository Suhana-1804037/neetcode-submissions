# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.ans = 0
        self.cal(root)
        return self.ans
    
    def cal(self, root)->int:
        if not root:
            return 0
        right = self.cal(root.right) if root.right else 0
        left = self.cal(root.left) if root.left else 0
        self.ans = max(self.ans, left+right)
        return 1+max(left, right)
        


