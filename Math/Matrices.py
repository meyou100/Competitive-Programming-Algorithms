def matmul(a, b, mod=-1):
    n = len(a)
    m = 1 if type(b[0]) == int else len(b[0])
    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(a[0])):
                if mod != -1:
                    res[i][j] = (a[i][k] * b[k][j] % mod + res[i][j]) % mod
                else:
                    res[i][j] += a[i][k] * b[k][j]
    return res

def power(a, k, mod=-1):
    res = -1
    while k > 1:
        if k % 2:
            if res == -1:
                res = a
            else:
                res = matmul(res, a, mod)
        a = matmul(a, a, mod)
        k >>= 1
    if res != -1:
        return matmul(a, res, mod)
    return a