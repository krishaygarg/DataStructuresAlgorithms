class Solution:
    def difference(self, w1, w2):
        for i in range(min(len(w1),len(w2))):
            if w1[i]!=w2[i]:
                print(w1[i],w2[i])
                return w1[i], w2[i]
        return None, None

    def foreignDictionary(self, words: List[str]) -> str:
        seen = set()
        outgoing = defaultdict(list)
        incoming = defaultdict(int)
        for i in range(len(words)-1):
            a, b = None, None
            w1 = words[i]
            w2 = words[i+1]
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    print(w1[j],w2[j])
                    a, b = w1[j], w2[j]
                    break
            if a is None and len(w1)>len(w2):
                return ""

            if a is not None:
                outgoing[a].append(b)
                incoming[b]+=1
                seen.add(a)
                seen.add(b)

        q = deque()
        for key in outgoing.keys():
            if incoming[key]==0:
                q.append(key)

        answer = ""
        while (len(q)>0):
            element = q.pop()
            answer+=element
            for i in outgoing[element]:
                incoming[i]-=1
                if incoming[i]==0:
                    q.append(i)
        if (len(answer)<len(outgoing.keys())):
            return ""
        for word in words:
            for char in word:
                if char not in seen:
                    answer+=char
                    seen.add(char)
        
        return answer
