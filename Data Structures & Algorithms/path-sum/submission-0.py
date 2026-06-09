# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def pathHelper(node, running_total):
            if not node:
                return False
            
            running_total += node.val

            if not node.left and not node.right and running_total == targetSum:
                return True
            if pathHelper(node.left, running_total):
                return True
            if pathHelper(node.right, running_total):
                return True
            
            running_total -= node.val
            return False
        
        return pathHelper(root, 0)