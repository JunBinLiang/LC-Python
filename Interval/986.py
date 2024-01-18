class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        n, m = len(a), len(b)
        i, j = 0, 0
        res = []
        
        def cross(a, b):
            if b[0] > a[1] or b[1] < a[0]:
                return []
            return [max(a[0], b[0]), min(a[1], b[1])]
        
        while i < n and j < m:
            interval = cross(a[i], b[j])
            if len(interval) > 0:
                res.append(interval)
            if a[i][1] <= b[j][1]:
                i += 1
            else:
                j += 1
                
        return res
