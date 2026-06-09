class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""

        for char in s:
            if char.isalnum():
                s2 += char

        s2 = s2.lower()

        reverse = ""
        for i in range(len(s2) - 1, -1, -1):
            reverse += s2[i]
            


        return  reverse == s2
