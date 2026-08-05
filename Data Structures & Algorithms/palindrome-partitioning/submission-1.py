import copy
class Solution:
    def checkPalindrome(self, s):
        left = 0
        right = len(s)-1
        while (left<=right):
            if (s[left]!=s[right]):
                return False
            left+=1
            right-=1
        return True

    def backtrack(self, i):
        # print(i,self.current,self.curstring)
        if (i==len(self.s)):
            if self.curstring!="":
                return
            for j in self.current:
                if (not self.checkPalindrome(j)):
                    return
            self.answer.append(copy.deepcopy(self.current))
            return
        original = self.curstring
        self.curstring+=self.s[i]
        self.current.append(self.curstring)
        self.curstring = ""
        self.backtrack(i+1)
        self.curstring = original
        self.current.pop()
        self.curstring+=self.s[i]      
        self.backtrack(i+1)
        self.curstring = original
        


    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.answer = []
        self.current = []
        self.curstring = ""
        self.backtrack(0)
        return self.answer