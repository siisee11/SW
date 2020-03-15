import numpy as np

t = []
t.append(np.array([[1, 1, 1, 1]]))
t.append(np.array([[1, 0], [1, 0], [1, 1]]))
t.append(np.array([[0, 1], [0, 1], [1, 1]]))
t.append(np.array([[1, 0], [1, 1], [0, 1]]))
t.append(np.array([[1, 1], [1, 1]]))
t.append(np.array([[1, 1, 1], [0, 1, 0]]))

def convolution2d(image, kernel, bias):
    m, n = kernel.shape
    y, x = image.shape
    y = y - m + 1
    x = x - n + 1
    new_image = np.zeros((y,x))
    for i in range(y):
        for j in range(x):
            new_image[i][j] = np.sum(image[i:i+m, j:j+n]*kernel) + bias

    return np.max(new_image)

if __name__ == "__main__":
    N, M = map(int, input().split())
    Matrix = [[0]*M for i in range(N)]

    for i in range(N):
        line = input().split()
        for j in range(M):
            Matrix[i][j] = int(line[j])
    Matrix = np.asarray(Matrix)

    max = 0
    for tet in t:
        for d in range(4):
            tet = np.rot90(tet, d)
            ret = convolution2d(Matrix, tet, 0)
            if max < ret :
                max = ret

    print(int(max))

    
