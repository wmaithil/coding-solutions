
class Graph:

    adj=[]

    def __init__(self,v,e):
        self.v=v
        self.e=e
        self.adj=[[0 for i in range(v)] for i in range(v)]

    def addEdge(self,s,e):
        self.adj[s][e]=1
        self.adj[e][s]=1

    def bfs(self,start):
        visited = [0 for i in range(self.v)]
        q=[]
        q.append(start)
        visited[start]=1
        
        while(q):
            curr=q[0]
            print(curr, end=" ")
            q.pop(0)
            
            for i in range(self.v):
                if self.adj[curr][i]== 1 and visited[i] == 0:
                    q.append(i)

                    visited[i]=1


v, e = 5, 4
 
# Create the graph
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(1, 3)
 
# Perform BFS
G.bfs(0)
 
                
            


