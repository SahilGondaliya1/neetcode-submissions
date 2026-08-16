class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force is doing two iteration
        # better approach is to use the hashing -> because it provides O(1) lookup time in python
        # hash_map = {}
        # for integer in nums:
        #     if integer in hash_map:
        #         return True
        #     hash_map[integer]=integer
        # return False
        # # time complexity -> O(N)
        # # space complexity -> O(1)

        # the another approach
        # the time : O(N)
        # the space : O(N)
        # we use hashset it is python specific solution
        hash_set = set(nums)
        if len(hash_set) != len(nums):
            return True
        return False

