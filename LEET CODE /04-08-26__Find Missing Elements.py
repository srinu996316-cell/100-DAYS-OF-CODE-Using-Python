class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smallest = min(nums)
        largest = max(nums)
        present = set(nums)

        return [
            number
            for number in range(smallest, largest + 1)
            if number not in present
        ]
