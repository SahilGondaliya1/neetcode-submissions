class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # need the frequency of the numbers
        
        # naive solution : 
        # we sort based on the frequency

        # we count the frequecy for the each element
        # we use array of length nums -> because frequency wont be more than the length

    
        freq_map = Counter(nums)
        # this is freq_map witht the elements

        # distinct elements
        dist_ele = list(freq_map.keys())

        dist_ele.sort(
            key=lambda num:freq_map[num],   
            reverse=True
        )

        return dist_ele[:k]

        
        
