from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ranks = defaultdict(int)
        for num in nums:
            ranks[num] += 1 
        sorted_by_val_desc = dict(sorted(ranks.items(), key = lambda item: item[1], reverse=True))


        return list(sorted_by_val_desc)[:k]
        