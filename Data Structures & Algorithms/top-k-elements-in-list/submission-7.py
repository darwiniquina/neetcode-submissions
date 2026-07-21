class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        frequencies_tuple = []

        for key, value in frequencies.items():
            frequencies_tuple.append((key, value))

        frequencies_tuple.sort(key=lambda frequency: frequency[1], reverse=True)


        output = []
        for value in frequencies_tuple:
            if len(output) == k:
                break

            output.append(value[0])
        
        return output

            
