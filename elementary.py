def dim(A):
    r, c = len(A), len(A[0])
    return r, c


def sum(A, B):
    result = None
    
    if dim(A) == dim(B):
        r, c = dim(A)
        result = [[0 for j in range(c)] for i in range(r)]    
        for i in range(r):
            for j in range(c):
                result[i][j] = A[i][j] + B[i][j]
    else:
        print("Dimension error.")
        
    return result

def sub(A, B):
    result = None
    
    if dim(A) == dim(B):
        r, c = dim(A)
        result = [[0 for j in range(c)] for i in range(r)]    
        for i in range(r):
            for j in range(c):
                result[i][j] = A[i][j] - B[i][j]
    else:
        print("Dimension error.")
        
    return result


def dot(A, B):
    result = None
    rA, cA = dim(A)
    rB, cB = dim(B)

    if cA == rB:
        result = [[0 for j in range(cB)] for i in range(rA)]
        for i in range(rA):
            for j in range(cB):
                for k in range(cA):
                    result[i][j] += A[i][k] * B[k][j]
                 
    else:
        print("Dimension error.")

    return result
                
        