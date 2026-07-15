from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        for word in strs:
            for group in res:
                if sorted(word) == sorted(group[0]):
                    group.append(word)
                    break
            else:
                res.append([word])

        return res
