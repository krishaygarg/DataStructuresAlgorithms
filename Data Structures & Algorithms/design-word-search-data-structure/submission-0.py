class Node:
    def __init__(self,val,ends):
        self.val = val
        self.next = [None]*26
        self.ends = ends
    def add(self,val,ends):
        if (self.next[ord(val)-ord('a')] is None):
            self.next[ord(val)-ord('a')] = Node(val,ends)

        return self.next[ord(val)-ord('a')]
    
class WordDictionary:
    def __init__(self):
        self.head = Node('a',False)


    def addWord(self, word: str) -> None:
        cur = self.head
        for letter in range(len(word)-1):
            cur = cur.add(word[letter],False)
        cur = cur.add(word[-1],True)

    def dfs(self,word,node,i):
        print(word,node.val,node.ends,i)
        if i == len(word):
            return node.ends
        if (word[i]!='.'):
            if node.next[ord(word[i])-ord('a')] is None:
                return False
            else:
                return self.dfs(word,node.next[ord(word[i])-ord('a')],i+1)
        else:
            found = False
            for j in range(len(node.next)):
                if (node.next[j] is not None):
                    if self.dfs(word,node.next[j],i+1):
                        found = True
            return found

    def search(self, word: str) -> bool:
        return self.dfs(word,self.head,0)

