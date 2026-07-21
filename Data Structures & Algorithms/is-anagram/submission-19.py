class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False


        s_key = [0] * 26
        t_key = [0] * 26

        for i in range(len(s)):
            s_item = s[i]
            t_item = t[i]

            s_ord = ord(s_item)
            t_ord = ord(t_item)

            base_ord = ord("a")

            s_key[s_ord - base_ord] += 1
            t_key[t_ord - base_ord] += 1

        if tuple(s_key) != tuple(t_key):
            return False

        return True

            