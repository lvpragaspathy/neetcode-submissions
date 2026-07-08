# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def swapChildren(node):
            temp = node.left
            node.left = node.right
            node.right = temp
        
        def processTree(node):
            if node == None:
                return
            
            swapChildren(node)
            processTree(node.left)
            processTree(node.right)
        
        processTree(root)

        return root

        