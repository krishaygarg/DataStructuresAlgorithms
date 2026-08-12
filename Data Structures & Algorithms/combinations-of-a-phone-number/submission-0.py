class Solution:
    def backtrack(self,i):
        if i==len(self.digits):
            if len(self.current)>0:
                self.answer.append("".join(self.current))
            return
        for char in self.mapping[self.digits[i]]:
            self.current.append(char)
            self.backtrack(i+1)
            self.current.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        self.answer = []
        self.current = []
        self.digits = digits
        self.mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        self.backtrack(0)
        return self.answer
