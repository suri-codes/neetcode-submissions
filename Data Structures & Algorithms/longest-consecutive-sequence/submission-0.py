class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set()
        for i in nums:
            hash.add(i)
        roots = []
        for i in nums:
            if (i-1) not in hash:
                roots.append(i)

        longest = 0
        for root in roots:
            root_length = 0
            for i in range(root, 100000, 1):
                if i in hash:
                    root_length+=1
                else:
                    break
            if longest < root_length:
                longest = root_length
        return longest