class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) 

        def helper(x) :
            return ord(x) - ord('a')

        for string in strs:
            profile = [0] * 26

            for char in string:
                profile[helper(char)] += 1

            groups[tuple(profile)].append(string)

        return list(groups.values())




            




        