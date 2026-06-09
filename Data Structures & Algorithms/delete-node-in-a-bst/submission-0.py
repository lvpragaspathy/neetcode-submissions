# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def minValueSubnode(root):
            curr = root
            while curr.left != None:
                curr = curr.left
            return curr


        if not node:
            return None
            
        if val > node.val:
            node.right = self.deleteNode(node.right, val)
        elif val < node.val:
            node.left = self.deleteNode(node.left, val)
        else:

            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            else:
                min_node = minValueSubnode(node.right)     
                node.val = min_node.val
                node.right = self.deleteNode(node.right, min_node.val)
                
        return node
        