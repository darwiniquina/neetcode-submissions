class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        items = {}

        for str_val in strs:
            sorted_text = "".join(sorted(str_val))

            if sorted_text not in items:
                items[sorted_text] = []

            items[sorted_text].append(str_val)

        return list(items.values())