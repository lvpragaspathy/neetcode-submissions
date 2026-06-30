# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Need to do a DFS
        def find_depth(node):
            if node is None:
                return -1

            left = find_depth(node.left)
            right = find_depth(node.right)

            return 1 + max(left, right)

        return find_depth(root) + 1
        







            

        