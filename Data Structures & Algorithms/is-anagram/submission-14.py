class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        c_index_1 = [0] * 26
        t_index_2 = [0] * 26

        for i in range(len(s)):
            base_ord = ord("a")

            s_item = s[i]
            t_item = t[i]

            s_index = ord(s_item)
            t_index = ord(t_item)
         
            c_index_1[s_index - base_ord] += 1
            t_index_2[t_index - base_ord] += 1

        print(c_index_1, t_index_2)
        return str(c_index_1) == str(t_index_2)

        