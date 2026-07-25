class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_r = len(grid)
        len_c = len(grid[0])

        queue = collections.deque()
        num_fresh = 0 
        time_elapsed = 0

        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    num_fresh += 1

        while queue and num_fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
            
                if r+1 < len_r and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    num_fresh -= 1
                    queue.append((r+1, c))
                    
                if r-1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    num_fresh -= 1
                    queue.append((r-1, c))

                if c+1 < len_c and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    num_fresh -= 1
                    queue.append((r, c+1))

                if c-1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    num_fresh -= 1
                    queue.append((r, c-1))

            time_elapsed += 1
            
        if num_fresh > 0:
            return -1 
        else:
            return time_elapsed
            



        

            




        