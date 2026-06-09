class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_map = {}
        

       # def alphabet_pos(x): # a = 0, z = 25
           # return ord(x) - 97

        for string in strs:
            profile = ''.join(sorted(string))
            if profile in output_map:
                output_map[profile].append(string)
            else:
                output_map[profile] = [string]

        return list(output_map.values())


        