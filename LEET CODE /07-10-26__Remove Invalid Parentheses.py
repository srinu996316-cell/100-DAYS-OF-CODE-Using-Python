class Solution(object):
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        result = []
        queue = {s}
        found = False

        while queue:
            # Check all strings at the current removal level
            for string in queue:
                if is_valid(string):
                    result.append(string)
                    found = True

            # Once valid strings are found, don't remove more characters
            if found:
                return result

            next_level = set()

            for string in queue:
                for i in range(len(string)):
                    # Only remove parentheses
                    if string[i] == '(' or string[i] == ')':
                        new_string = string[:i] + string[i + 1:]
                        next_level.add(new_string)

            queue = next_level

        return result
