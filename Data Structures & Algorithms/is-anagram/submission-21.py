class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_ord_output = [0] * 26
        t_ord_output = [0] * 26
        base_ord = ord("a")

        for i in range(len(s)):
            s_ord = ord(s[i])
            t_ord = ord(t[i])

            s_pointer = s_ord - base_ord
            t_pointer = t_ord - base_ord

            s_ord_output[s_pointer] += 1
            t_ord_output[t_pointer] += 1

        if str(s_ord_output) != str(t_ord_output):
            return False
            
        return True
                    