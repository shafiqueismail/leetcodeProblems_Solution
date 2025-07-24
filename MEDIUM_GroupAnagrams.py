class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # This is from a librabry called collections. 
                                # It’s like a normal dictionary ({}), but it makes empty lists automatically
        for s in strs:
            sortedS = ''.join(sorted(s)) # we add the ''.join(sorted(s)) since its right now in a list and we want it in string form.
            res[sortedS].append(s) # sortedS is the key, and s is the actual letter
        return list(res.values())
