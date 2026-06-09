# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insertHelper(curr_node, key):
            if key > curr_node.val:
                if curr_node.right:
                    insertHelper(curr_node.right, key)
                else:
                    curr_node.right = TreeNode(key)
            else:
                if curr_node.left:
                    insertHelper(curr_node.left, key)
                else:
                    curr_node.left = TreeNode(key)

        if root is None:
            root = TreeNode(val)
            return root
            
        insertHelper(root, val)

        return root
        