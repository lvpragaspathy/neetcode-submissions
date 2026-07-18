import pandas as pd

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        longest_found = 1
        freq = defaultdict(int)
        freq[s[l]] = 1
        max_freq = 1

        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            if (r - l + 1) > longest_found:
                    longest_found = (r - l + 1)

            r += 1

        return longest_found
                


