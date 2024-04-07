import elementary as el
import lup

class CompositionMatrix:
    def __init__(self, rm):
        self.r = rm # stores all the representative matrices
        self.d = len(rm)
        self.n = len(rm[0])
        
    def __add__(self, other):
        result = []
        for i in range(self.d):
            result.append(el.sum(self.r[i], other.r[i]))
        return CompositionMatrix(result)

    def __sub__(self, other):
        result = []
        for i in range(self.d):
            result.append(el.sub(self.r[i], other.r[i]))
        return CompositionMatrix(result)

    def __mul__(self, other):
        result = []
        for i in range(self.d):
            result.append(el.dot(self.r[i], other.r[i]))
        return CompositionMatrix(result)

    def __invert__(self):
        result = []
        for i in range(self.d):
            result.append(lup.inv(self.r[i]))
        return CompositionMatrix(result)

    def transform(self):
        dim = self.d * self.n
        result = [[0 for j in range(dim)] for i in range(dim)]
        for k in range(self.d):
            for i in range(self.n):
                for j in range(self.n):
                    result[k+i*self.d][k+j*self.d] = self.r[k][i][j]

        return result
