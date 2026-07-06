from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        # Count each number
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 0

            num_dict[num] += 1

        # Get both the number and frequency
        items = list(num_dict.items())

        # Sort using the frequency: item[1]
        items.sort(key=lambda item: item[1], reverse=True)

        output = []

        # Take the first k numbers
        for num, frequency in items:
            output.append(num)

            if len(output) == k:
                break

        return output