from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        if not text1 or not text2:
            return 0

        mem = defaultdict(int)
        
        #i: text1 pointer, j: text2 pointer
        @cache
        def dp(i, j) -> int:
            if i > len(text1)-1 or j > len(text2)-1:
                return 0
            
            if (i, j) in mem:
                return mem[(i, j)]

            if text1[i] == text2[j]:
                mem[(i, j)] = 1 + dp(i+1, j+1)

            else:
                mem[(i, j)] = max(dp(i+1, j), dp(i, j+1))

            return mem[(i, j)]

        return dp(0, 0)

