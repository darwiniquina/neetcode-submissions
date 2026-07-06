class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped = []

        for value in strs:
            placed = False
            key = sorted(value)

            for group in grouped:
                if key == sorted(group[0]):
                    group.append(value)
                    placed = True
                    break

            if not placed:
                grouped.append([value])

        return grouped