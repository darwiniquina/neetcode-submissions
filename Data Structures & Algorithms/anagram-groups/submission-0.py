class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        base_ord = ord("a")

        grouped_dict = {}

        for value in strs:

            value_key = [0] * 26

            # Loop each string to create a key
            for character in value:
                character_index = ord(character) - base_ord

                value_key[character_index] += 1

            final_value_key = tuple(value_key)

            if final_value_key not in grouped_dict:
                grouped_dict[final_value_key] = []

            grouped_dict[final_value_key].append(value)

        return ( list(grouped_dict.values()))                
            

                

