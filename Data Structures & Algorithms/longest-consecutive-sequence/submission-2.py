class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        
        longest_seq= 0
        for num in set_of_nums:
            if num-1 not in set_of_nums:
                seq_length = 1
                n = num+1
                
                while n in set_of_nums:
                    seq_length += 1
                    n += 1

                if seq_length > longest_seq:
                    longest_seq = seq_length

        return longest_seq
                


        


        

        


        
            
            