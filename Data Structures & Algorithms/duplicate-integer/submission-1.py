class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l_set = set(nums) #deduplication
        return len(l_set) != len(nums)       