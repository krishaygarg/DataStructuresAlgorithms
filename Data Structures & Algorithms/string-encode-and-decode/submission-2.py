class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for string in strs:
            encoding+=str(len(string))
            encoding+="#"
            encoding+=string
        print(encoding)
        return encoding
    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while (i<len(s)):
            current_str = ""
            string_length = ""
            while (s[i]!="#"):
                string_length+=s[i]
                i+=1
            string_length = int(string_length)
            i+=1
            for j in range(string_length):
                current_str+=s[i]
                i+=1
            answer.append(current_str)

        return answer