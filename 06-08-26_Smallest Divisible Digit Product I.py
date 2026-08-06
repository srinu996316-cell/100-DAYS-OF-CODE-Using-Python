class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def digit_product(x):
            product = 1
            for ch in str(x):
                product *= int(ch)
            return product

        while True:
            if digit_product(n) % t == 0:
                return n
            n += 1
