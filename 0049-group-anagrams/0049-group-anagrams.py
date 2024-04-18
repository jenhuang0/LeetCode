class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupana = defaultdict(list)

        for s in strs:
            groupname = str(sorted(s))
            groupana[groupname].append(s)
        return (groupana.values())