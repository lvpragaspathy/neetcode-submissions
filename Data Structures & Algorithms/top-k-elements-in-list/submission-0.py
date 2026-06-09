class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = [0 for i in range(len(set(nums)))]
        tallies = dict(zip(set(nums), counter))
        
        for num in nums:
            tallies.update({num: tallies.get(num) + 1})
        
        maxes = []

        for i in range(0, k):
            this = max(tallies, key=tallies.get)
            maxes.append(this)
            del tallies[this]


        return(maxes)