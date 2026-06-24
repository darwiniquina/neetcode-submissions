class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        missed = 0
        my_dict = {}

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            string_1 = s[i]
            string_2 = t[i]

            if string_1 not in my_dict:
                my_dict[string_1] = 0

            if string_2 not in my_dict:
                my_dict[string_2] = 0

            my_dict[string_1] = my_dict[string_1] + 1
            
            my_dict[string_2] = my_dict[string_2] - 1

        for key, value in my_dict.items():
            if value > 0:
                return False

        return True




