class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = {}

        for value in strs:
            key_ord = [0] * 26

            for char in value:
                base_ord = ord("a")

                key_ord[ord(char) - base_ord] += 1

            key_ord = tuple(key_ord)
            if key_ord not in output:
                output[key_ord] = []
            
            output[key_ord].append(value)

        return list(output.values())
                
                