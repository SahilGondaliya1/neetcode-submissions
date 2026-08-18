class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # frequecy map
        freq_map = {}
        for index , i in enumerate(nums):
            compliment = target - i
            if compliment in freq_map:
                return [freq_map[compliment], index]
            freq_map[i] = index

        return [0,1]



