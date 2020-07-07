# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
# 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

from collections import deque

bridge_length = int(input())
weight = int(input())
truck_weights = deque(map(int, input().split()))

on_board = deque([0]*bridge_length)
time = 0
total = 0

while truck_weights:
    time += 1

    if on_board[0] != 0:
        print("차가 나가야 할 때입니다.")
        total -= on_board.popleft()
        on_board.appendleft(0)
        print(f"나간 후 남은 차들은 {on_board}")

    on_board.popleft()

    if total + truck_weights[0] <= weight:
        total += truck_weights[0]
        on_board.append(truck_weights.popleft())
        print(f"현재 다리를 건너고 있는 차들은 : {on_board}")
        print(f"남은 차들은 : {truck_weights}")
    else:
        on_board.append(0)
        print(f"현재 다리를 건너고 있는 차들은 : {on_board}")
        print(f"남은 차들은 : {truck_weights}")
    print(f"현재 시각은 {time}초")

print(f"마지막 차가 들어온 시각은 {time}초")

print(f"총 걸린 시간은 {time+bridge_length}초")