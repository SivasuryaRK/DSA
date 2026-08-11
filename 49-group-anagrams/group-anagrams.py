class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for s in strs:
            so = "".join(sorted(s))
            if so not in a:
                a[so] = []
            a[so].append(s)
        return list(a.values())

        # {
        #     'aet': ["eat"]
                # 'abt': []
        # }