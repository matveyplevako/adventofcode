LENGTH = 10007

deck = list(range(LENGTH))


def mat_identity(N):
    return [[1 if i == j else 0 for j in range(N)] for i in range(N)]


def mat_mult(A, B, mod=0):
    N = len(A)
    M = len(B[0])

    L = len(A[0])
    assert L == len(B)

    C = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            acc = 0
            for k in range(L):
                acc += A[i][k] * B[k][j]
            if mod != 0:
                acc %= mod
            C[i][j] = acc

    return C


def mat_pow(A, exp, mod=0):
    res = mat_identity(2)
    while exp > 0:
        if exp % 2 == 1:
            res = mat_mult(res, A, mod)
        A = mat_mult(A, A, mod)
        exp //= 2
    return res


with open("input.txt") as inp:
    MOD = 119315717514047
    REP = 101741582076661

    a = 1
    b = 0

    for instruction in inp.readlines():
        if "new" in instruction:
            a *= -1
            b = -b - 1
        if "cut" in instruction:
            cut = int(instruction.split()[-1])
            b -= cut
        if "increment" in instruction:
            inc = int(instruction.split()[-1])
            a *= inc
            b *= inc

    a = a % MOD
    b = b % MOD
    inv_a = pow(a, MOD - 2, MOD)
    inv_b = ((-b) * inv_a) % MOD

    M = [[inv_a, inv_b], [0, 1]]

    Mexp = mat_pow(M, REP, MOD)

    v = [[2020], [1]]
    y = mat_mult(Mexp, v, MOD)

print(y[0][0])
