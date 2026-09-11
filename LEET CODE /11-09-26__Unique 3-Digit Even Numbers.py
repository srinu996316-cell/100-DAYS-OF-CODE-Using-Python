class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        count = 0

        for a in range(1, 10):       # Hundreds digit
            for b in range(10):      # Tens digit
                for c in range(0, 10, 2):  # Units digit must be even

                    number = [a, b, c]

                    # Check if these digits can be formed
                    temp = digits[:]
                    possible = True

                    for d in number:
                        if d in temp:
                            temp.remove(d)
                        else:
                            possible = False
                            break

                    if possible:
                        count += 1

        return count
