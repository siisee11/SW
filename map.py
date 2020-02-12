def solution(n, arr1, arr2):
    answer = []

    for r1, r2 in zip(arr1, arr2):
        row = ""
        for i in range(n - 1, -1, -1):
            row += ('#' if (r1 | r2) & (2 ** i) != 0 else ' ')
        answer.append(row)

    return answer