class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m, i is rows; n, j is cols
        #prevRow = [0]  * n

        def dp(prevRow, k) -> int:
            if k < 0:
                return prevRow[0]

            currRow = [0] * n
            currRow[-1] = 1

            i = n-1
            j = n-2
            while j >= 0:
                currRow[i-1] = prevRow[j] + currRow[i]
                i -= 1
                j -= 1

            return dp(currRow.copy(), k-1)

        return dp([0] * n, m-1)

