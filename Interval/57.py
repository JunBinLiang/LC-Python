class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #intervals.append(newInterval)
        #intervals.sort()
        #stk = []
        #for interval in intervals:
        #    if len(stk) > 0 and interval[0] <= stk[len(stk) - 1][1]:
        #        stk[len(stk) - 1][1] = max(stk[len(stk) - 1][1], interval[1])
        #    else:
        #        stk.append(interval)
        #return stk
        
        stk = []
        n = len(intervals)
        index = n
        for i in range(n):
            if intervals[i][0] < newInterval[0]:
                stk.append(intervals[i])
            else:
                index = i
                break
    
        if len(stk) > 0 and newInterval[0] <= stk[len(stk) - 1][1]:
            stk[len(stk) - 1][1] = max(stk[len(stk) - 1][1], newInterval[1])
        else:
            stk.append(newInterval)
            
        for i in range(index, n):
            interval = intervals[i]
            if len(stk) > 0 and interval[0] <= stk[len(stk) - 1][1]:
                stk[len(stk) - 1][1] = max(stk[len(stk) - 1][1], interval[1])
            else:
                stk.append(interval)
                
        return stk
