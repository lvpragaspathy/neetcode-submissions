class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        working = [0] * 3

        print(triplets)
        #for triplet in triplets: # get rid of irrelevent triplets
           # print("checking... ", triplet)
            #for i in range(3):
                #print("checking... ", triplet[i], " vs ", target[i])
               # if triplet[i] > target[i]:
                    #print("discarding... " , triplet)
                    #triplets.pop(i)

       # print(triplets)
        for triplet in triplets:
            
            if (triplet[0] > target[0]) or (triplet[1] > target[1]) or (triplet[2] > target[2]):
                continue

            working = [max(working[0], triplet[0]), max(working[1], triplet[1]), max(working[2], triplet[2])]
            print("working... ", working)
        
        print("target... ", target)
        return working == target #?
            

        