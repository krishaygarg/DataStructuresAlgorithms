class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        positions = dict()
        for i in range(len(s)):
            if s[i] not in positions:
                positions[s[i]] = [i,i]
            else:
                positions[s[i]][1] = i
        l = list(positions.values())
        l.sort()
        sizes = []
        current = 0
        start = 0
        print(l)
        for i in range(len(l)):
            if l[i][0]>current:
                sizes.append(l[i][0]-start)
                start = l[i][0]
            current = max(current, l[i][1])
        sizes.append(current-start+1)
        return sizes