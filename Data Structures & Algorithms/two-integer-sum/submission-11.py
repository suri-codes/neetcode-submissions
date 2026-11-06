class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}
        for idx, num in enumerate(nums):
            recip = target-num
            

            maybe = map.get(recip)

            if maybe is not None:
                return [maybe, idx]
            else:
                map[num]=idx


