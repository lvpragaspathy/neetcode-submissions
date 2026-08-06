# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        hashmap = defaultdict(lambda: (0, 0))
        stack = [root]

        while stack:
            curr = stack[-1]
            lsub = curr.left
            rsub = curr.right

            if lsub and lsub not in hashmap:
                stack.append(lsub)
            elif rsub and rsub not in hashmap:
                stack.append(rsub)
            else:
                stack.pop()
                lheight, ldiam = hashmap[lsub]
                rheight, rdiam = hashmap[rsub]

                hashmap[curr] = (1 + max(lheight, rheight), max(lheight + rheight, ldiam, rdiam))

        return hashmap[root][1]
            



