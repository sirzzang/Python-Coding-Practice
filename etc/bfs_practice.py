'''
BFS 구현 방법
1. 그래프 표현: 해당 노드를 key, 해당 노드에 인접한 노드들의 리스트를 value로 하는 dict.
2. 큐 사용: 방문해야 할 지점. 먼저 방문해야 할 곳 순서대로 쭉 방문한 후, 아래로 내려 간다.
'''

# 1. 기본 구현
'''
- 방문 시: pop(0)
- 방문해야 할 노드 queue: 리스트.
'''
def BFS_1(graph, start_node):
    visited = [] # 방문한 노드
    queue = [start_node] # 정점 노드로 시작
    while queue:
        cur = queue.pop(0)
        print(f"현재 노드: {cur}")
        if cur not in visited: # 아직 방문하지 않았을 경우
            visited.append(cur) # 방문 후
            queue.extend(graph[cur]) # 방문해야 할 노드 추가.
        print(f"현재 방문 지점: {visited}, 방문해야 할 노드: {queue}")
    return visited

# 2. set 활용: 순서가 바뀌는 문제를 해결해야 한다.
'''
- 이미 방문한 곳을 중복하여 queue에 쌓는 문제가 있다.
- 따라서 set을 활용하여 방문해야 할 곳을 추가해 보자.
'''
def BFS_2(graph, start_node):
    visited = []
    queue = [start_node]
    while queue:
        cur = queue.pop(0)
        print(f"현재 노드: {cur}")
        if cur not in visited:
            visited.append(cur)
            queue.extend(graph[cur] - set(visited)) # 순서 주의
        print(f"현재 방문 지점: {visited}, 방문해야 할 노드: {queue}")
    return visited

# 3. deque 활용
'''
- pop(0)은 시간이 오래 걸린다.
- deque을 이용해 시간복잡도를 낮춰 보자.
'''
from collections import deque
def BFS_3(graph, start_node):
    visited = []
    queue = deque([start_node])
    while queue:
        cur = queue.popleft() # 시간복잡도 줄어듦.
        print(f"현재 노드: {cur}")
        if cur not in visited:
            visited.append(cur)
            queue.extend(graph[cur])
        print(f"현재 방문 지점: {visited}, 방문해야 할 노드: {queue}")
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


    # print(BFS_1(graph, 'A'))
    # print(BFS_2(graph, 'A'))
    print(BFS_3(graph, 'A'))