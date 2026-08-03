class Solution:
    def backtrack(self, l, r):
        if (l==0 and r==0):
            self.answer.append("".join(self.current))
            return
        if (l>0):
            self.current.append("(")
            self.backtrack(l-1,r)
            self.current.pop()
        if (r>0 and r>l):
            self.current.append(")")
            self.backtrack(l,r-1)
            self.current.pop()
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []
        self.current = []
        self.backtrack(n,n)
        return self.answer