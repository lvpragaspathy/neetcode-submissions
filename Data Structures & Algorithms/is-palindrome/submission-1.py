class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""

        for char in s:
            if char.isalnum():
                s2 += char

        s2 = s2.lower()

        return  s2 == s2[::-1]
