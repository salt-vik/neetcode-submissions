from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for source,destination,weight in times:
            adj[source].append([destination,weight])
        dist=[float('inf')]*(n+1)
        visited=[0]*(n+1)
        dist[k]=0
        pq=[(0,k)]
        while(pq):
            distance,node=heappop(pq)
            if visited[node]==1:
                continue
            visited[node]=1
            for nxt,weight in adj[node]:
                if dist[nxt]>distance+weight and visited[nxt]==0:
                    dist[nxt]=distance+weight
                    heappush(pq,(dist[nxt],nxt))
        if float('inf') in dist[1:]:
            return -1
        else:
            return max(dist[1:])

                
