class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        min_eating = 1
        while ( s<=e):
            mid = (s+e)//2
            hours =0 
            for i in piles:
                if i % mid == 0:
                    hours = hours + (i//mid)
                else:
                    hours = hours + (i//mid) + 1
                
            if hours <=h:
                min_eating = mid
                e = mid-1
            else:
                s = mid +1
        return s