class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        queue = collections.deque()

        def getNexts(r, c, length): 
            for row in range(r-1, r+2):
                for col in range(c-1, c+2):
                    if row == r and col == c:
                        continue
                    
                    if row < 0 or row > n-1 or col < 0 or col > n-1:
                        continue

                    if grid[row][col] == 0:
                        queue.append([row, col, length+1])
                        grid[row][col] = 1

        queue.append([0, 0, 1])
        grid[0][0] = 1

        while queue:
            r, c, length = queue.popleft()
                
            if r == n-1 and c == n-1:
                return length

            getNexts(r, c, length)

        return -1
        
                




            

        