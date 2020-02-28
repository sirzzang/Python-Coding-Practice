# 코드 1 ~ 코드 5까지의 경우는 엄청난 시행착오가 있었다.
# 시행착오를 정리하면 다음과 같다.
# 1) 레이저를 바꿔준다. : 이 단계까지는 문제가 없다.
# 2) 레이저로 쇠막대를 자르고, 자른 쇠막대는 세지 않는다.
# - 일단 쇠막대의 시작(왼쪽 괄호)을 stack에 push하고, 쇠막대의 끝(오른쪽 괄호)이 나오면 그 사이에 있는 레이저의 개수를 바탕으로 조각의 개수를 저장한 뒤, stack에서 pop한다.
# 3) 중첩된 쇠막대가 어떻게 잘리게 되는지 개수를 센다. : 이 단계에서 엄청난 문제를 겪었다.
# - 최종적으로 정착한 방법은 다음과 같다.
# - Laser의 차례가 될 때, Laser을 누적과 현재로 나누어 개수를 센다.
# - 누적 Laser의 개수는 괄호가 닫힐 차례(오른쪽 괄호가 나올 때)에 안에 남은 쇠막대가 없다면, 개수를 세는 데에 활용된다.
# - 현재 Laser의 개수는 현재 층의 쇠막대, 즉, 열린 괄호 기점으로 가장 안쪽에 있는 쇠막대의 개수를 세는 데에 활용된다.
# - 이 때 현재 Laser의 개수를 세는 데에 경우의 수를 나눠줘야 해서 힘들었다.
# - L이 나오는 경우를 다음과 같이 분류할 수 있다.
# --- stack이 빈 경우 : 자를 쇠막대가 없으므로 laser 개수로 세지 않는다.
# --- stack이 비지 않은 경우
# ------ "(L" : 무조건 현재 laser의 개수를 1로 만든다. 가장 처음 나온 레이저이기 때문이다.
# ------ ")L" : 현재 laser의 개수를 0으로 초기화한다. 이미 쇠막대가 하나 사용되었기 때문이다.
# ------ "LL" : 현재 laser의 개수를 1 더해준다.
# - 그렇다면, 현재 laser의 개수가 0이라면 가장 안쪽에 있는 쇠막대는 사용했다는 의미가 된다. 현재 laser의 개수가 1 이상일 때에만 현재 laser의 개수가 의미가 있다.
# - 또한, stack이 빈다면, 사용할 수 있는 쇠막대를 모두 만들어 사용했다는 의미이므로, laser의 개수를 초기화한다. 현재 laser 개수이든, 누적 laser 개수이든 모두 초기화한다.
# 4) 최종적으로, 다음과 같이 잘려진 막대 조각 개수를 구한다.
# - 현재 laser가 있는 경우, 안쪽 쇠막대가 있다는 의미이므로, 현재 laser에 의해 잘린 조각을 더한다.
# - 현재 laser가 없는 경우, 안쪽 쇠막대는 이미 다 사용했으므로, 다음 층 쇠막대가 누적 laser에 의해 잘린 조각을 더한다.

# 코드 5. -> 다른 방법 다시 생각하자.
# 제출 : 틀렸습니다.

# L 들어올 때, stack이 비어 있는지 검사하고, 안 비어 있다면(왼쪽 괄호가 하나라도 나왔다는 말이므로), 왼쪽 괄호만 나왔다면 초기화하도록!
# 현재 레이저는, 반드시 오른쪽 괄호가 나오고 난 뒤나, 오른쪽 괄호가 나오지 않았다면 가장 최근에 나온 왼쪽 괄호의 경우에만 + 해야 함.

import sys
stick_input = sys.stdin.readline().strip('\n')
sticks = stick_input.replace("()", "L") # ()를 laser로 변환

stack = []
laser_cum = 0 # 누적 laser 수
laser_cur = 0 # 현재 laser 수
stick_pieces = 0 # 쇠막대 조각 수

for i in range(len(sticks)):

    if len(stack) == 0:
        laser_cum = 0
        laser_cur = 0
    
    else: # stack에 쇠막대의 시작이 있는 상태
        if sticks[i] == "(": # 쇠막대의 시작(왼쪽 괄호)을 stack에 push
            stack.append(sticks[i])
    
        elif sticks[i] == "L": # 쇠막대의 시작이 stack에 들어 있는 경우에만 laser의 개수를 센다.
            laser_cum += 1 # 레이저가 나오면 누적 laser 개수를 올린다.
            if sticks[i-1] == "(": # 현재 laser 개수를 경우에 따라 저장한다.
                laser_cur = 1
            elif sticks[i-1] == ")":
                laser_cur = 0
            else:
                laser_cur += 1          
    
        else: # 쇠막대의 끝(오른쪽 괄호)이 오면,
            if laser_cur == 0: # 현재 laser의 개수가 없는 경우, 안쪽 쇠막대는 다 사용했다는 의미이므로 바깥쪽 쇠막대를 사용한다.
                stick_pieces += (laser_cum + 1) # 바깥쪽 쇠막대는 누적 laser에 의해 잘리게 된다.
                stack.pop() # 자르고 난 뒤 쇠막대의 왼쪽을 stack에서 pop

            else:
                stick_pieces += (laser_cur + 1) # 현재 laser가 있는 경우, 현재 laser에 의해 잘리는 조각의 수를 더하고
                stack.pop() # 쇠막대 시작 없애고
                laser_cur = 0 # 현재 laser는 초기화한다.          

print(stick_pieces)


# 코드 4.
# L이 들어올 때, 바로 앞에 오른쪽 괄호가 온 경우라면, 즉 막대가 하나 닫힌 경우라면 현재 레이저 개수를 올리지 않도록 해보자.
# 일단 이러면, 첫 번째 경우에는 17이 제대로 맞게 출력된다.
# 두 번째 경우에 24가 아니라 26이 나온다;;;
# 아우 시댕...........................
# L 받을 때 왼쪽 괄호 있으면 현재 레이저 개수 초기화해야 한다.

stick_input = input()
sticks = stick_input.replace("()", "L")
print(sticks)

stack = []
laser_cum = 0 # 누적 레이저 개수
laser_cur = 0 # 현재 레이저 개수
stick_pieces = 0

for i in range(len(sticks)):
    
    print(f"{i}번째 loop")

    if sticks[i] == "(":
        stack.append(sticks[i])
        print(f"{i}번째 stack은 {stack}")
        print(f"{i}번째 누적 레이저 개수는 {laser_cum}")
        print(f"{i}번째 현재 레이저 개수는 {laser_cur}")
        print(f"{i}번째 stick 개수는 {stick_pieces}")
    
    elif sticks[i] == "L":
        if len(stack) != 0:
            laser_cum += 1 # 누적 레이저 개수 올리기
            if sticks[i-1] != ")":
                laser_cur += 1 # 현재 레이저 개수 올리기
        print(f"{i}번째 stack은 {stack}")
        print(f"{i}번째 누적 레이저 개수는 {laser_cum}")
        print(f"{i}번째 현재 레이저 개수는 {laser_cur}")
        print(f"{i}번째 stick 개수는 {stick_pieces}")
    
    else: # 오른쪽 괄호 들어오는 경우
        if laser_cur == 0:
            stick_pieces += (laser_cum + 1)
            stack.pop()
            print(f"{i}번째 stack은 {stack}")
            print(f"{i}번째 누적 레이저 개수는 {laser_cum}")
            print(f"{i}번째 현재 레이저 개수는 {laser_cur}")
            print(f"{i}번째 stick 개수는 {stick_pieces}")
        else:
            stick_pieces += (laser_cur + 1)
            stack.pop()
            if len(stack) == 0:
                laser_cum = 0
                laser_cur = 0
            print(f"{i}번째 stack은 {stack}")
            print(f"{i}번째 누적 레이저 개수는 {laser_cum}")
            print(f"{i}번째 현재 레이저 개수는 {laser_cur}")
            print(f"{i}번째 stick 개수는 {stick_pieces}")

print(stick_pieces)

# 코드 3
# 누적 레이저와 현재 레이저의 수로 생각해본다.
# 현재 레이저 -> 누적 레이저로 바꾸는 구분선이 필요해서 구분자로 slash를 쓸까 생각했는데, pop할 수 없다는 문제점이 있고, 다시 append하는 거 자체를 구현하기 어려움.
# 현재 레이저 개수가 0이고, 바로 ")"가 나오면 누적 레이저 개수 +1 더해준다.
# stack이 비게 되면, 누적 레이저 개수 0으로 초기화한다.
# 일단 오른쪽 괄호가 먼저 들어오는 경우는 없다고 가정하고 프로그래밍한다. 막대기가 된다는 거 자체가 왼쪽이 먼저 들어와야 하는 거니까.
# 이렇게 짜니까 14
# 단계별로 뜯어보니까, 현재 레이저가 0이라는 조건이 붙을 경우에만 누적 레이저 절단 개수를 더하므로, L((L))(L)에서 '(LL)(L)'을 빼버리고 난 뒤의 ')L' 이 부분이 문제가 된다.

stick_input = input()
sticks = stick_input.replace("()", "L")
print(sticks)

stack = []
laser_cum = 0 # 누적 레이저 개수
laser_cur = 0 # 현재 레이저 개수
stick_pieces = 0


for i in range(len(sticks)):
    
    if sticks[i] == "(":
        stack.append(sticks[i])

    elif sticks[i] == "L":
        if len(stack) != 0:
            laser_cum += 1 # 누적 레이저 개수 올리기
            laser_cur += 1 # 현재 레이저 개수 올리기
    
    else: # 오른쪽 괄호 들어오는 경우
        if laser_cur == 0:
            stick_pieces += (laser_cum + 1)
        else:
            if len(stack) == 0:
                laser_cum == 0
                laser_cur == 0

            else:
                stick_pieces += (laser_cur + 1)
                stack.pop()
                laser_cur = 0

print(stick_pieces)

# 코드 2
# laser 개수로 바꾸기는 했는데, 이것도 여전히 문제가 있다.
# 17개 출력해야 하는데 19개가 출력된다.
# 단계별로 뜯어보니, L(((LL)(L)L))(L)에서 (LL)를 지우고 (L)를 지워야 할 때, laser 개수가 그대로 count된다.
# 레이저 개수를 누적 레이저 개수와, 현재 레이저 개수로 나눠야 하지 않을까?
# 그리고, 애초에 누적 레이저 0일 경우를 생각해주지 않아도 된다! -> 일단 오른쪽 괄호가 남아 있다면, L을 다 바꾸고 남은 걸테니까 L이 반드시 있을 수밖에 없다!

stick_input = input()
sticks = stick_input.replace("()", "L")

stack = []
laser_cnt = 0
stick_pieces = 0

for i in range(len(sticks)):

    if sticks[i] == "(":
        stack.append(sticks[i])

    elif sticks[i] == "L":
        if len(stack) != 0:
            laser_cnt += 1

    else:
        if laser_cnt == 0: # 레이저가 없으면
            stack.pop()

        else: # 레이저가 있으면
            stick_pieces += (laser_cnt +1)
            stack.pop()
    
    if len(stack) == 0:
        laser_cnt = 0

# 코드 1
# laser 구현까지는 됐는데, 나중에 출력하니까 조각의 개수가 0이 나온다.
# loop 내 index별로 뭐가 문제인지 알아보기 위해 단계마다 print한 결과, 
# else 부분에서, 막대 개수를 더해주는 게 안 된다.
# 당연하다! stack에 laser을 안 받았으니까!!!!!!

stick_input = input()
sticks = stick_input.replace("()", "L")
print(sticks)

stack = []
laser_cnt = 0
stick_pieces = 0

for i in range(len(sticks)):

    if sticks[i] == "(":
        stack.append(sticks[i])

    elif sticks[i] == "L":
        if len(stack) != 0:
            laser_cnt += 1

    else:
        if stack[-1] != "L": # 레이저가 없으면
            stack.pop()

        else: # 레이저가 있으면
            stick_pieces += (laser_cnt +1)
            stack.pop()
    
    if len(stack) == 0:
        laser_cnt = 0