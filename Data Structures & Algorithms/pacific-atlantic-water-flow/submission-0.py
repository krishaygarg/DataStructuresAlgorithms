class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        visited1 = [[0]*n for _ in range(m)] 
        visited2 = [[0]*n for _ in range(m)] 
        q = []
        for i in range(m):
            q.append([i,0])
        for i in range(n):
            q.append([0,i])
        while (len(q)>0):
            element = q.pop()
            visited1[element[0]][element[1]] = 1
            if (element[0]>0 and heights[element[0]-1][element[1]]>=heights[element[0]][element[1]]
             and visited1[element[0]-1][element[1]]==0):
                q.append([element[0]-1,element[1]])
            if (element[1]>0 and heights[element[0]][element[1]-1]>=heights[element[0]][element[1]]
            and visited1[element[0]][element[1]-1]==0):
                q.append([element[0],element[1]-1])
            if (element[0]<m-1 and heights[element[0]+1][element[1]]>=heights[element[0]][element[1]]
            and visited1[element[0]+1][element[1]]==0):
                q.append([element[0]+1,element[1]])
            if (element[1]<n-1 and heights[element[0]][element[1]+1]>=heights[element[0]][element[1]]
            and visited1[element[0]][element[1]+1]==0):
                q.append([element[0],element[1]+1]) 
        for i in range(m):
            q.append([i,n-1])
        for i in range(n):
            q.append([m-1,i])
        while (len(q)>0):
            element = q.pop()
            visited2[element[0]][element[1]] = 1
            if (element[0]>0 and heights[element[0]-1][element[1]]>=heights[element[0]][element[1]]
             and visited2[element[0]-1][element[1]]==0):
                q.append([element[0]-1,element[1]])
            if (element[1]>0 and heights[element[0]][element[1]-1]>=heights[element[0]][element[1]]
            and visited2[element[0]][element[1]-1]==0):
                q.append([element[0],element[1]-1])
            if (element[0]<m-1 and heights[element[0]+1][element[1]]>=heights[element[0]][element[1]]
            and visited2[element[0]+1][element[1]]==0):
                q.append([element[0]+1,element[1]])
            if (element[1]<n-1 and heights[element[0]][element[1]+1]>=heights[element[0]][element[1]]
            and visited2[element[0]][element[1]+1]==0):
                q.append([element[0],element[1]+1])  
        answer = [] 
        for i in range(m):
            for j in range(n):
                if visited1[i][j] and visited2[i][j]:
                    answer.append([i,j])  
        print(visited1,visited2)             
        return answer
