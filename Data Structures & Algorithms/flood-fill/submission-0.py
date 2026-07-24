class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:  
        scolor = image[sr][sc]

        if color == scolor:
            return image

        m_rows = len(image)
        n_cols = len(image[0])


        def flood(r, c):
            image[r][c] = color

            if r-1 >= 0 and image[r-1][c] == scolor:
                flood(r-1, c)

            if r+1 < m_rows and image[r+1][c] == scolor:
                flood(r+1, c)

            if c-1 >= 0 and image[r][c-1] == scolor:
                flood(r, c-1)
            
            if c+1 < n_cols and image[r][c+1] == scolor:
                flood(r, c+1)
            
            return

        flood(sr, sc)

        return image
