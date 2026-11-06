from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for strr in strs:
            hsh = "".join(sorted(strr))
            groups[hsh].append(strr)

        return list(groups.values())