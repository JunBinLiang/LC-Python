class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))
        stk = []
        for interval in intervals:
            s, e = interval[0], interval[1]
            if len(stk) > 0 and stk[len(stk) - 1][1] >= s:
                if stk[len(stk) - 1][1] >= e:
                    pass
                else:
                    stk.append(interval)
            else:
                stk.append(interval)      
        return len(stk)
