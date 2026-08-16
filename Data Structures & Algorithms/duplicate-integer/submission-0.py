class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force is doing two iteration
        # better approach is to use the hashing -> because it provides O(1) lookup time in python
        hash_map = {}
        for integer in nums:
            if integer in hash_map:
                return True
            hash_map[integer]=integer
        return False
