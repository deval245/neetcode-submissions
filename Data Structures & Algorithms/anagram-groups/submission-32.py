class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grp = dict ()

        for ch in strs:
            key = ''.join(sorted(ch))

            if key not in grp:
                grp[key] = []
            grp[key].append(ch)   
        return list(grp.values())