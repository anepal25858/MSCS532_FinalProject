def matmul_naive(A, B):
    n = len(A)
    X = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                X[i][j] += A[i][k] * B[k][j]
    return X

def matmul_tiled(A, B, tileSize):
    n = len(A)
    X = [[0] * n for _ in range(n)]
    for a in range(0, n, tileSize):
        for b in range(0, n, tileSize):
            for c in range(0, n, tileSize):
                for i in range(a, min(a + tileSize, n)):
                    for j in range(b, min(b + tileSize, n)):
                        for k in range(c, min(c + tileSize, n)):
                            X[i][j] += A[i][k] * B[k][j]
    return X

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
tileSize = 1

naive = matmul_naive(A, B)
tiled = matmul_tiled(A, B, tileSize)

print("Naive:", naive)
print("Tiled:", tiled)
