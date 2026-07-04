class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        letters = set()
        l, r, largest_found = 0, 1, 0
        letters.add(s[l])

        while r < len(s):
            if s[r] not in letters:
                letters.add(s[r])
                largest_found = max(largest_found, r - l + 1)
                r += 1        
            else:
                while s[r] in letters:
                    letters.remove(s[l])
                    l += 1
                letters.add(s[r])  
                largest_found = max(largest_found, r - l + 1)
                r += 1         
        return largest_found



        