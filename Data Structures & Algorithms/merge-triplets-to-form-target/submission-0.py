class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # find a subset so that target is maximum of each
        found = [0,0,0]
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            for i in range(3):
                if t[i]==target[i]:
                    found[i]=True
        return bool(found[0] and found[1] and found[2])
            