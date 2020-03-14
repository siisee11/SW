snake = [(1, 1)]
dir_dic = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
HEAD = 0

if __name__ == "__main__":
    N = int(input())
    K = int(input())
    apples = [tuple(map(int, input().split())) for _ in range(K)]

    Matrix = {(x,y):-1 for x in range(N + 2) for y in range(N + 2)}
    for x in range(1, N + 1, 1):
        for y in range(1, N + 1, 1):
            Matrix[(x, y)] = 0
    for apple in apples:
        Matrix[apple] = 2

    time = 0
    Matrix[snake[HEAD]] = 1
    direction = 0

    L = int(input())
    turn = [input().split() for _ in range(L)]

    while True:
        time += 1
        next = tuple(map(sum, zip(snake[HEAD], dir_dic[direction])))

        # 다음 위치가 몸과 부딪히거나 벽에 닿음
        if Matrix[next] == -1 or next in snake:
            break

        # 가능하다면 머리를 위치시키고 꼬리를 뺌
        snake.insert(HEAD, next)
        if Matrix[snake[HEAD]] != 2:
            snake.pop()

        # 방향 전환
        if turn and time == int(turn[0][0]):
            if turn[0][1] == 'L':
                direction = (direction + 3) % 4
            else : 
                direction = (direction + 1) % 4
            turn.pop(0)

    print(time)