class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        string_counter = {}
        string_total = 0

        for i in s:
            if i not in string_counter:
                string_counter[i] = 0

            string_counter[i] += 1
            string_total += 1

        for i in t:
            #E
            if i not in string_counter:
                return False
            else: 
                string_counter[i] -= 1
                string_total -= 1

                #E
                if string_counter[i] < 0:
                    return False

        return string_total == 0

