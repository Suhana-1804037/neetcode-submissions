# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def func(root: Optional[TreeNode] )->int:
            if not root:
                return float("-inf")
            nonlocal ans
            leftVal = func(root.left)
            rightVal = func(root.right)
            rootVal = root.val
            val = max(rootVal, rootVal+leftVal, rootVal + leftVal + rightVal, rootVal+rightVal)
            path = max(rootVal + leftVal, rootVal + rightVal, rootVal)

            ans = max(ans, val, path)
            return path
        value = func(root)
        return ans