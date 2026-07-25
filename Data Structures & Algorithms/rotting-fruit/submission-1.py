class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_r = len(grid)
        len_c = len(grid[0])

        def isAdjToRot(r, c):
            if r+1 < len_r and grid[r+1][c] == 2:
                return True

            if r-1 >= 0 and grid[r-1][c] == 2:
                return True

            if c+1 < len_c and grid[r][c+1] == 2:
                return True

            if c-1 >= 0 and grid[r][c-1] == 2:
                return True

            return False

        def containsFresh():
            for row in grid:
                for col in row:
                    if col == 1:
                        return True

            return False
            
        contains_rot = True
       
        time_elapsed = 0

        while True:
            to_update = []

            for row in range(len_r):
                for col in range(len_c):
                    if grid[row][col] == 1 and isAdjToRot(row, col):
                        to_update.append((row, col))

            if len(to_update) == 0:
                break
        
            for r, c in to_update:
                grid[r][c] = 2

            time_elapsed += 1

        if containsFresh():
            return -1
        else:
            return time_elapsed

        

            




        