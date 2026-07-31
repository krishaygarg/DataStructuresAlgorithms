class Solution:
    def sort(self, string):
        l = list(string)
        l.sort()
        return "".join(l)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for i in strs:
            m[self.sort(i)].append(i)
        answer = []
        for _,val in m.items():
            answer.append(val)
        return answer