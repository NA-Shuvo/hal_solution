def exchange(a, b):
    temp = b
    b = a
    a = temp
    return a, b


def lup_decompose(X):

    n = len(X)
    A = [[X[i][j] for j in range(n)] for i in range(n)]
    pi = [i for i in range(n)]

    for k in range(n):
        p = 0
        for i in range(k,n):
            if abs(A[i][k]) > p :
                p = abs(A[i][k])
                k0 = i
        if p == 0:
            break

        pi[k], pi[k0] = exchange(pi[k], pi[k0])

        for i in range(n):
            A[k][i], A[k0][i] = exchange(A[k][i], A[k0][i])

        for i in range(k+1, n):
            A[i][k] = A[i][k]/A[k][k]
            for j in range(k+1, n):
                A[i][j] = A[i][j] - A[i][k] * A[k][j]

        # P L U
        P = [[0 for j in range(n)] for i in range(n)]
        L = [[0 for j in range(n)] for i in range(n)]
        U = [[0 for j in range(n)] for i in range(n)]
        
        for i in range(n):
            P[i][pi[i]] = 1

        for i in range(n):
            for j in range(n):
                if i>j:
                    L[i][j] = A[i][j]
                else:
                    U[i][j] = A[i][j]
        for i in range(n):
            L[i][i] = 1
                
                
        

    return P, pi, L, U



def lup_solve(L, U, pi, b):
    n = len(L)
    x, y = [0 for i in range(n)], [0 for i in range(n)]
    
    for i in range(n):
        s = 0
        for j in range(i):
            s += L[i][j] * y[j]
        y[i] = b[pi[i]] - s
    
        
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1,n):
            s += U[i][j] * x[j]
        x[i] = (y[i] - s)/U[i][i]

    return x



def identity_mat(n):
    I = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                I[i][j] = 1
    return I



def inverse(A, L, U, pi):
    n = len(A)
    invA = [[0 for j in range(n)] for i in range(n)]
    I = identity_mat(n)
    
    for i in range(n):
        invA[i] = lup_solve(L, U, pi, I[i])

    return invA

def inv(A):
    P, pi, L, U = lup_decompose(A)
    return inverse(A, L, U, pi)
