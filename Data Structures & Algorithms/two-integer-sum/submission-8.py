class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_i, i in enumerate(nums):   
            for inner, j in enumerate(nums[idx_i+1:]):
                idx_j = idx_i + 1 + inner
                if i + j == target:
                     return [idx_i,idx_j]
  
        