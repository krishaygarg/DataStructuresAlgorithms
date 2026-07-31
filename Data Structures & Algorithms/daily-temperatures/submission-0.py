class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0]*n
        for i in range(n):
            print(stack)
            while (len(stack)!=0 and stack[-1][0]<temperatures[i]):
                element = stack.pop()
                answer[element[1]]=i-element[1]
            stack.append([temperatures[i],i])
        return answer