class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        first = last = -1
        minimum = float('inf')
        
        prev = head
        curr = head.next
        pos = 1
        
        while curr and curr.next:
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):
                
                if first == -1:
                    first = pos
                else:
                    minimum = min(minimum, pos - last)
                
                last = pos
            
            prev = curr
            curr = curr.next
            pos += 1
        
        if first == last:
            return [-1, -1]
        
        return [minimum, last - first]
