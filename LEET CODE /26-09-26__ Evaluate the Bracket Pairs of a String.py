class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        
        # Convert knowledge into a dictionary
        values = {}
        for key, value in knowledge:
            values[key] = value
        
        result = []
        i = 0
        
        while i < len(s):
            if s[i] == '(':
                # Find the closing bracket
                j = i + 1
                while s[j] != ')':
                    j += 1
                
                # Extract the key
                key = s[i + 1:j]
                
                # Replace with value if known, otherwise '?'
                if key in values:
                    result.append(values[key])
                else:
                    result.append("?")
                
                # Move past ')'
                i = j + 1
            
            else:
                result.append(s[i])
                i += 1
        
        return ''.join(result)
