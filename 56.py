class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stk = []
        for interval in intervals:
            if len(stk) > 0 and interval[0] <= stk[len(stk) - 1][1]:
                stk[len(stk) - 1][1] = max(stk[len(stk) - 1][1], interval[1])
            else:
                stk.append(interval)
        return stk
