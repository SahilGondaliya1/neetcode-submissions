class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force -> 2 loops -> checking the length of array , and variable maintaining maximum lengrh.
        # better approach here is improving those loops -> we use conditional looping ,
        # now for the first index -> we start the checks when the check breaks we update the starting index to breaking one. it is a kind of two pointer approach.
    #    
        hash_set = set(nums)
        
        start_of_index = {}

        for integer in nums:
            if integer-1 not in hash_set:
                start_of_index[integer] = 1

        
        for start in start_of_index.keys():
            next =True
            value = start
            while next:

                if value+1 in hash_set:
                    start_of_index[start] = start_of_index[start]+1
                    value += 1 
                else:
                    next=False                
            
        max = 0
        for count in start_of_index.values():
            if count  > max : 
                max = count            
                
        return max



