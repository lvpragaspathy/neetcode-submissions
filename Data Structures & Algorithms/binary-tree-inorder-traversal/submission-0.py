# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        
        def inorderHelper(node):
            if not node:
                return
            inorderHelper(node.left)
            traversal.append(node.val)
            inorderHelper(node.right)
        
        inorderHelper(root)

        return traversal