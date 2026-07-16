class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = {}

        for word in strs:
            key = [0] * 26

            for letter in word:
                base_ord = ord('a')
                letter_ord = ord(letter)

                key[letter_ord - base_ord] += 1
            
            tuple_key = tuple(key)
            if tuple_key not in output:
                output[tuple_key] = []

            output[tuple_key].append(word)

        return list (output.values())

                
            
      