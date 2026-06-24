class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        working = [0] * 3

        for triplet in triplets:
            if (triplet[0] > target[0]) or (triplet[1] > target[1]) or (triplet[2] > target[2]):
                continue

            working = [max(working[0], triplet[0]), max(working[1], triplet[1]), max(working[2], triplet[2])]        

        return working == target 
            

        