
inf=10**5
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph= [[0 for i in range(self.v)]for i in range(self.v)]

    def minDist(self,dist,visited):
        mindist=inf
        
        for j in range(self.v):
            if(visited[j]==False and mindist>dist[j]):
                mindist=dist[j]
                minindex=j
                
        return minindex

    def dijkstra(self,src):
 
        dist= [inf for i in range(self.v)]
        dist[src]=0

        parent=[-1 for i in range(self.v)]
        visited= [False for i in range(self.v)]
      
        for _ in range(self.v):
            V=self.minDist(dist,visited)
            visited[V]=True
        
            for j in range(self.v):
                if(self.graph[V][j]!= 0 and visited[j]== False and dist[j]>self.graph[V][j]+dist[V]):
                    dist[j]=self.graph[V][j]+dist[V]
                    parent[j]=V
                    
        print("The dist array is",dist)
        print(parent)
    


#main     
g=Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
 
g.dijkstra(0)

        