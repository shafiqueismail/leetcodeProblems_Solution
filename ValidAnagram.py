class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_update = sorted(s)
        t_update = sorted(t)

        if (s_update == t_update):
            return True
        else:
            return False
