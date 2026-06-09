class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for string in strs:
            key = tuple(sorted(string))
            if key in output:
                output[key].append(string)
            else:
                output[key] = [string]

        return list(output.values())


        