# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        pq = collections.deque()
        qq = collections.deque()
        pq.append(p)
        qq.append(q)

        while pq and qq:
            pcurr = pq.popleft()
            qcurr = qq.popleft()

            if not pcurr and not qcurr:
                continue

            if pcurr and not qcurr:
                return False

            if qcurr and not pcurr:
                return False

            if pcurr.val != qcurr.val:
                return False

            pq.append(pcurr.left)
            pq.append(pcurr.right)
            qq.append(qcurr.left)
            qq.append(qcurr.right)  

        return True

            
        