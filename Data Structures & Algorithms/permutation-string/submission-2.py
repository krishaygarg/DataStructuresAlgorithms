class Solution:
    def check(self,f1, f2):
        for key, value in f1.items():
            if (f2[key]!=value):
                return False
        for key, value in f2.items():
            if (f1[key]!=value):
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        s1freq = defaultdict(int)
        s2freq = defaultdict(int)
        for i in range(len(s1)):
            s1freq[s1[i]]+=1
            s2freq[s2[i]]+=1
        for i in range(len(s2)-len(s1)+1):
            print(s1freq,s2freq)
            if (self.check(s1freq,s2freq)):
                return True
            if (i!=len(s2)-len(s1)):
                s2freq[s2[i]]-=1
                s2freq[s2[len(s1)+i]]+=1
        return False