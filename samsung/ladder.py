def find_valid(cols, i):
    col = cols[i]
    if i == 0:
        return [i for i,x in enumerate(col) if x != 1 and x != -1]
    ans = []
    prev_col = cols[i - 1]
    for j in range(len(col)):
        if col[j] != -1 and col[j] != 1:
            if prev_col[0:j].count(1) % 2 == 0 :
                ans.append(j)
    return ans


def find_position(cols, ncols, cur):
    if (ncols == len(cols) - 1):
        return 1
    col = cols[ncols]
    valid_positions = find_valid(cols, ncols)
    print(valid_positions)

    if col.count(1) % 2 == 0 :
        return find_position(cols, ncols+1, cur)
    else:
        for position in valid_positions:
            col[position] = cur
            check_invalid(cols, ncols)
            if find_position(cols, ncols+1, cur) == 0 :
                col[position] = -1
            else:
                return 1
    return 0

def check_invalid(cols, i):
    col = cols[i]
    next_col = cols[i + 1]

    if col.count(1) % 2 == 0:
        for i in range(len(col)):
            if col[i] != 1:
                col[i] = -1

    for j in range(len(col)):
        if col[j] >= 1:
            next_col[j] = -1
        if next_col[j] >= 1:
            col[j] = -1

if __name__ == "__main__":
    N, M, H = map(int, (input().split()))
    ladders = [tuple(map(int, input().split())) for _ in range(M)]

    cols = [[0] * (H) for i in range(N)]
    for ladder in ladders:
        cols[ladder[1] - 1][ladder[0] - 1] = 1

    for i in range(len(cols) - 1):
        check_invalid(cols, i)

    cur = 2
    if (find_position(cols, 0, cur) == 1):
        print(cols)
        print(sum(col.count(cur) for col in cols))
    else:
        print("-1")