class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        str_dict = {}
        string_total = 0
        
        #E
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char not in str_dict:
                str_dict[s_char] = 0

            if t_char not in str_dict:
                str_dict[t_char] = 0

            str_dict[s_char] += 1
            str_dict[t_char] -= 1

        for index, i in str_dict.items():
            if i != 0:
                return False
        return True