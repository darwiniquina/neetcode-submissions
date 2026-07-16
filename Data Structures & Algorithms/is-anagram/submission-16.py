class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        az_1 = [0] * 26
        az_2 = [0] * 26

        for i in range(len(s)):
            base_ord = ord('a')

            s_ord = ord(s[i])
            t_ord = ord(t[i])

            az_1[s_ord - base_ord] += 1
            az_2[t_ord - base_ord] += 1

        return tuple(az_1) == tuple(az_2)

