class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        # No stones with remainder 1 or 2
        if cnt[1] == 0 and cnt[2] == 0:
            return False

        # Even number of stones divisible by 3
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # Odd number of stones divisible by 3
        return abs(cnt[1] - cnt[2]) > 2
