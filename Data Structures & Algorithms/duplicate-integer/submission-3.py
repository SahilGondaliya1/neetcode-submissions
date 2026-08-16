class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force is doing two iteration

        # the another approach
        # the time : O(N)
        # the space : O(N)
        # we use hashset it is python specific solution
        hash_set = set(nums)
        if len(hash_set) != len(nums):
            return True
        return False

