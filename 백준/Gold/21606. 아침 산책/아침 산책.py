import sys
sys.setrecursionlimit(10**6)

N = int(input())
inside = '0' + input()

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
total = 0

for _ in range(N-1):
    a,b =map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

    if inside[a] == "1" and inside[b] == "1": #예제에서 [4] [5]만 해당
        total += 2
        
def dfs(start):
    visited[start] = True
    inside_count = 0
    for v in graph[start]:  #graph[2]에 들어있는 1,3,4만 구경하고 나옴 
        if inside[v] == '1':
            inside_count += 1

        elif not visited[v] and inside[i] == "0":
            inside_count += dfs(v)

    return inside_count

for i in range(1, N+1):
    if inside[i] == '0' and not visited[i]:
        result = dfs(i)  # 2만 dfs하면 이코드는 끝남
        total += (result) * (result-1)

print(total)