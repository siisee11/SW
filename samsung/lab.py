import copy
from itertools import combinations

dir_dic = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

def virus(board, initial_viruses, min_virus, walls) :
    cur_virus = len(initial_viruses)
    viruses = initial_viruses

    for wall in walls :
        board[wall] = 1

    while True:
        if len(viruses) == 0:
            break
        virus = viruses.pop(0)
        if min_virus < cur_virus:
            return min_virus
        for direction in range(4) :
            next = tuple(map(sum, zip(virus, dir_dic[direction])))
            if board[next] == 0:
                board[next] = 2
                viruses.append(next)
                cur_virus += 1

    return cur_virus

if __name__ == "__main__" :
    N, M = map(int, input().split())
    min_virus = 1000
    initial_wall = 3
    initial_viruses = []

    idx = []

    board = {(x,y):1 for x in range(N + 2) for y in range(M + 2)}
    for x in range(1, N + 1, 1):
        line = list(map(int, input().split()))
        for y in range(1, M + 1, 1):
            board[(x, y)] = line[y - 1]
            if line[y - 1] == 2:
                initial_viruses.append((x, y))
            elif line[y - 1] == 1:
                initial_wall += 1
    
    for i in range(1, N+1) :
        for j in range(1, M+1) :
            if board[(i,j)] == 0 :
                idx.append((i, j))
    combi = list(combinations(idx, 3))

    for walls in combi :
        ret = virus(copy.deepcopy(board), copy.deepcopy(initial_viruses), copy.deepcopy(min_virus), walls)
        min_virus = ret if ret < min_virus else min_virus

    print(N * M - min_virus - initial_wall)