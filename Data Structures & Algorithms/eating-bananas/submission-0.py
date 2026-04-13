import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)  # left starts at 1 to avoid division by zero
        answer = right  # Initialize with the max possible speed
        
        while left <= right:
            mid = (left + right) // 2
            totalTime = 0
            
            for p in piles:
                totalTime += math.ceil(p / mid)  # No need for float() in Python 3
            
            if totalTime <= h:
                # If Koko can finish in <= h hours, try a smaller speed
                answer = mid
                right = mid - 1
            else:
                # If too slow, increase speed
                left = mid + 1
        
        return answer    