# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def func(root):
            if not root:
                ans.append("N")
                return 
            ans.append(str(root.val))
            func(root.left)
            func(root.right)
        func(root)
        return ",".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        value = data.split(",")
        self.i = 0

        def func():
            if value[self.i]=="N":
                self.i +=1
                return None
            node = TreeNode(int(value[self.i]))
            self.i+=1
            node.left = func()
            node.right = func()
            return node
        return func()




















