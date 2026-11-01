
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        moves = 0

        for num in nums:
            moves += num - minimum

        return moves
