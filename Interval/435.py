import heapq as hq
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        h = []
        pre_max = 0
        for interval in intervals:
            s, e = interval[0], interval[1]
            while len(h) > 0:
                x = hq.heappop(h)
                if x[0] <= s:
                    pre_max = max(pre_max, x[1])
                else:
                    hq.heappush(h, x) 
                    break
            hq.heappush(h, [e, 1 + pre_max]) 
            res = max(res, 1 + pre_max)
          
        return len(intervals) - res
            
