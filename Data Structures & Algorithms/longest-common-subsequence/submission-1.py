from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # For any character in text1, we need to find if it exists in text2  after the pointer. We need to chose if we want to keep it or not


        
        if not text1 or not text2:
            return 0
        
        # i: text1 pointer, j: text2 pointer
        @cache
        def dp(lcs, i, j) -> int:
            if i > len(text1)-1 or j > len(text2)-1:
                return lcs

            if text1[i] == text2[j]:
                return dp(lcs+1, i+1, j+1)

            else:
                return max(dp(lcs, i+1, j), dp(lcs, i, j+1))


        return dp(0, 0, 0)

