class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        def code_str(x: str):
            out = ""
            out += str(len(x))
            out += "#"
            out += x
            return out

        for string in strs:
            encoded_str += code_str(string)

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        
        while i < (len(s)):
            j = s.find('#', i)
            n = int(s[i: j])
            curr_str = s[j+1 : j+n+1]
            decoded_strs.append(curr_str)
            i = j + n + 1

        return decoded_strs

                









