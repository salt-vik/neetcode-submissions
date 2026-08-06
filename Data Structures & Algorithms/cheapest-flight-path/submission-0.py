class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF=float('inf')
        dist=[INF]*(n+1)
        dist[src]=0
        for _ in range(k+1):
            prev=dist[:]
            for u,v,w in flights:
                if dist[v]>prev[u]+w:
                    dist[v]=prev[u]+w
        if dist[dst]==INF:
            return -1
        else:
            return dist[dst]