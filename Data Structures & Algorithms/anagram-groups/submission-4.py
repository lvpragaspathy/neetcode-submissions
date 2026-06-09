class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        def letter_index(x):
            return ord(x) - ord('a') # 'a' will be at pos 0, 'z' at 25

        for string in strs:
            profile = [0] * 26

            for char in string:
                profile[letter_index(char)] += 1
            
            output[tuple(profile)].append(string)

        return list(output.values())


        