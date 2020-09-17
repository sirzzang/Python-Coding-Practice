'''
[DFS]
- 일단 한 컴퓨터가 걸리면,
- 거기랑 연결되어 있는 컴퓨터는 전부 다 걸리므로,
- 그 컴퓨터에서 연결되는 모든 컴퓨터들을 다 확인한 후,
- 다음 컴퓨터와 연결된 컴퓨터들을 탐색해야 한다.
'''


def make_graph(num_of_edges):
    graph = {}
    for _ in range(num_of_edges):
        edges = input().split()
        e1, e2 = edges[0], edges[1]
        if e1 not in graph:
            graph[e1] = [e2]
        elif e2 not in graph[e1]:
            graph[e1].append(e2)
        if e2 not in graph:
            graph[e2] = [e1]
        elif e1 not in graph[e2]:
            graph[e2].append(e1)
    return graph

def dfs(graph, root):
    infected = []
    stack = [root]
    while stack:
        cur_node = stack.pop()
        if cur_node not in infected:
            infected.append(cur_node)
            stack.extend(list(set(graph[cur_node]) - set(infected))) # 중복 제거
    return infected


n = int(input())
m = int(input())
g = make_graph(m)
print(g)
print(len(dfs(g, '1')) - 1)


