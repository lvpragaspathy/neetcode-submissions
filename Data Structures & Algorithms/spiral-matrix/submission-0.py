class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        total_length = m * n # total length
        output = []
        bearing = "east"
        i, j = 0, 0
        row_bounds = (0, m)
        col_bounds = (0, n)
        l = 0

        while l < total_length:
            if bearing == "east":
                left, right = col_bounds
                if j < right:
                    output.append(matrix[i][j])
                    l += 1 
                    j += 1
                    continue
                else:
                    bearing = "south"
                    top, down = row_bounds
                    row_bounds = (top+1, down) # finished that row
                    i, j = i+1, j-1

            elif bearing == "south":
                top, down = row_bounds
                left, right = col_bounds
                if i < down:
                    output.append(matrix[i][j])
                    l += 1 
                    i += 1
                    continue
                else:
                    bearing = "west"
                    col_bounds = (left, right-1) # finished that col
                    i, j = i-1, j-1

            elif bearing == "west":
                top, down = row_bounds
                left, right = col_bounds
                if j >= left:
                    output.append(matrix[i][j])
                    l += 1 
                    j -= 1
                    continue
                else:
                    bearing = "north"
                    row_bounds = (top, down-1) # finished that row
                    i, j = i-1, j+1

            else: # bearing == "north"
                top, down = row_bounds
                left, right = col_bounds
                if i >= top:
                    output.append(matrix[i][j])
                    l += 1 
                    i -= 1
                    continue
                else:
                    bearing = "east"
                    col_bounds = (left+1, right) # finished that col
                    i, j = i+1, j+1   

        return output





        