# 왜 자꾸 런타임에러가 날까

# # 1. 유향그래프 주의
# from collections import deque
# def make_graph(num):
#     graph = {}
#     for _ in range(num):
#         a, b = map(int, input().split())
#         # a와 연결된 정점
#         if a not in graph:
#             graph[a] = [b]
#         elif b not in graph[a]:
#             graph[a].append(b)
#         # b와 연결된 정점
#         if b not in graph:
#             graph[b] = [a]
#         elif a not in graph[b]:
#             graph[b].append(a)
#     return graph
#
# def dfs(graph, root):
#     visited = []
#     stack = [root]
#     while stack:
#         current = stack.pop()
#         if current not in visited:
#             visited.append(current)
#             temp = list(set(graph[current]) - set(visited)) # 중복 방문 제외
#             temp.sort(reverse=True) # 작은 수를 먼저 방문해야 함.
#             stack += temp
#     return visited
#
# def bfs(graph, root):
#     visited = []
#     queue = deque(set(root))
#     while queue:
#         current = queue.popleft()
#         if current not in visited:
#             visited.append(current)
#             temp = list(set(graph[current]) - set(visited)) # 중복 방문 제외
#             temp.sort() # 작은 수를 먼저 방문해야 함.
#             queue += temp
#     return visited
#
# n, m, v = map(int, input().split())
#
# g = make_graph(m)
# if v not in g: # 예외: 시작점 연결된 간선이 없을 때
#     print(v)
#     print(v)
# else:
#     print(*dfs(g, v))
#     print(*bfs(g, v))



# 1. 틀린 풀이
'''
node를 정렬해서 만드려고 하면 안 된다.
양 방향으로 그래프 만드는 과정에서 간선 간 연결 잘못될 수 있음.
'''

# def make_graph(nodes):
#     graph = {}
#     for node in nodes:
#         a, b = node[0], node[1]
#         # a와 연결된 정점
#         if a in graph:
#             graph[a].append(b)
#         else:
#             graph[a] = [b]
#         # b와 연결된 정점
#         if b in graph:
#             graph[b].append(a)
#         else:
#             graph[b] = [a]
#     return graph
#
# def dfs(graph, root):
#     visited = []
#     stack = [root]
#     while stack:
#         current = stack.pop()
#         if current not in visited:
#             visited.append(current)
#             stack += graph[current]
#     return ' '.join(visited)
#
# def bfs(graph, root):
#     from collections import deque
#     visited = []
#     queue = deque([root])
#     while queue:
#         current = queue.popleft()
#         if current not in visited:
#             visited.append(current)
#             queue += graph[current]
#     return ' '.join(visited)
#
# n, m, v = input().split()
# nodes = [list(input().split()) for _ in range(int(m))]
# nodes.sort(key=lambda x: int(x[1])) # BFS용 정렬
# g_bfs = make_graph(nodes)
# nodes.sort(key=lambda x: int(x[1]), reverse=True) # DFS용 정렬
# g_dfs = make_graph(nodes)
#
# print(dfs(g_dfs, v))
# print(bfs(g_bfs, v))