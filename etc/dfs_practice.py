'''
DFS 구현 방법
1. 그래프 표현: 해당 노드를 key, 해당 노드에 인접한 노드들의 리스트를 value로 하는 dict.
2. 스택 사용: 방문해야 할 지점. 먼저 방문한 곳에 연결되어 있는 노드를 아래로 쭉 본 후, 옆으로 간다.
'''

# 기본 구현: 오른쪽부터 간다.
def DFS(graph, start_node):
    visited = [] # 방문한 노드
    stack = [start_node] # 정점 노드로 시작
    while stack:
        cur = stack.pop()
        print(f"현재 노드: {cur}")
        if cur not in visited: # 아직 방문하지 않았을 경우
            visited.append(cur) # 방문 후
            stack.extend(graph[cur]) # 방문해야 할 노드 추가.
        print(f"현재 방문 지점: {visited}, 방문해야 할 노드: {stack}")
    return visited

# 왼쪽부터 가도록 구현하려면?
def DFS_2(graph, start_node):
    visited = []
    stack = [start_node]
    while stack:
        cur = stack.pop()
        print(f"현재 노드: {cur}")
        if cur not in visited:
            visited.append(cur)
            stack.extend(reversed(graph[cur]))
        print(f"현재 방문 지점: {visited}, 방문해야 할 노드: {stack}")
    return visited

# 테스트
if __name__ == '__main__':
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }


    # print(DFS(graph, 'A'))
    print(DFS_2(graph, 'A'))
