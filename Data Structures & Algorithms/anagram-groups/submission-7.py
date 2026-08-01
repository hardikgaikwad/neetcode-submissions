class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: dict[str, list[str]] = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')]+=1
            key = ", ".join(map(str, count))
            if key not in res:
                res[key] = []
            res[key].append(s)
        
        return list(res.values())