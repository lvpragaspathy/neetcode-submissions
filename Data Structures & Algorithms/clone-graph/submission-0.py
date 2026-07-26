"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clone = defaultdict(Node)
        queue = collections.deque()
        clone[node] = Node(val=node.val)
    
        for neighbor in node.neighbors:
            if neighbor not in clone:
                clone[neighbor] = Node(val=neighbor.val)
                queue.append(neighbor)

            clone[node].neighbors.append(clone[neighbor])


        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in clone:
                    queue.append(neighbor)
                    clone[neighbor] = Node(val=neighbor.val)
                
                clone[curr].neighbors.append(clone[neighbor])

        return clone[node]





        



            

            



        