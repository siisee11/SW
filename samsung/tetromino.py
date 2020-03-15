t = []
t.append([[1, 1, 1, 1]])
t.append([[1, 0], [1, 0], [1, 1]])
t.append([[0, 1], [0, 1], [1, 1]])
t.append([[1, 0], [1, 1], [0, 1]])
t.append([[0, 1], [1, 1], [1, 0]])
t.append([[1, 1], [1, 1]])
t.append([[1, 1, 1], [0, 1, 0]])

# Matrix dot 연산
def dot(mat, kernel):
    y, x = len(mat), len(mat[0])
    ret = 0
    for i in range(y):
        for j in range(x):
            ret += mat[i][j] * kernel[i][j]
    return ret

# Convolution 결과 중 가장 큰 element 반환
def convolution2d(image, kernel):
    m, n = len(kernel), len(kernel[0])
    y, x = len(image), len(image[0])
    y = y - m + 1
    x = x - n + 1
    max = 0
    for i in range(y):
        for j in range(x):
            sub = [x[j:j+n] for x in image[i:i+m]]
            sum = dot(sub, kernel)
            max = sum if sum > max else max

    return max

if __name__ == "__main__":
    N, M = map(int, input().split())
    Matrix = [list(map(int, input().split())) for _ in range(N)]

    max = 0
    for tet in t:
        for d in range(4):
            ret = convolution2d(Matrix, tet)
            max = ret if max < ret else max
            tet = list(zip(*tet[::-1]))

    print(int(max))