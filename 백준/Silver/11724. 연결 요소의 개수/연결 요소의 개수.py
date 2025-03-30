import sys
sys.setrecursionlimit(5000)
# dfs 함수
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n,m = map(int,sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u] += [v]
    graph[v] += [u]

count = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)
