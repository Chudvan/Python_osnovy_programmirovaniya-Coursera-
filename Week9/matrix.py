from copy import deepcopy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class MatrixError2(BaseException):
    def __init__(self, matrix1, other):
        self.matrix1 = matrix1
        self.other = other


class Matrix:
    def __init__(self, myLines):
        self.matrixLines = deepcopy(myLines)

    def size(self):
        numLines = len(self.matrixLines)
        numCols = len(self.matrixLines[0])
        return((numLines, numCols))

    def __str__(self):
        matrixList = []
        for line in self.matrixLines:
            matrixList.append('\t'.join(map(str, line)))
        return '\n'.join(matrixList)

    def __add__(self, other):
        if isinstance(other, Matrix):
            size = self.size()
            if size == other.size():
                def iPlusJ(i, j):
                    return self.matrixLines[i][j] + other.matrixLines[i][j]
                matrixList = []
                for i in range(size[0]):
                    matrixList.append([0] * size[1])
                for i in range(size[0]):
                    for j in range(size[1]):
                        matrixList[i][j] = iPlusJ(i, j)
                return Matrix(matrixList)
            raise MatrixError(self, other)
        raise MatrixError2(self, other)

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            size = self.size()
            matrixList = []
            for i in range(size[0]):
                matrixList.append([0] * size[1])
            for i in range(size[0]):
                for j in range(size[1]):
                    matrixList[i][j] = self.matrixLines[i][j] * other
            return Matrix(matrixList)
        elif isinstance(other, Matrix):
            size1 = self.size()
            size2 = other.size()
            if size1[1] == size2[0]:
                def iMulJ(i, j):
                    sumIJ = 0
                    matrix2Lines = other.returnMatrix()
                    for k in range(size1[1]):
                        sumIJ += self.matrixLines[i][k] * matrix2Lines[k][j]
                    return sumIJ
                matrixList = []
                for i in range(size1[0]):
                    matrixList.append([0] * size2[1])
                for i in range(size1[0]):
                    for j in range(size2[1]):
                        matrixList[i][j] = iMulJ(i, j)
                return Matrix(matrixList)
            raise MatrixError(self, other)
        raise MatrixError2(self, other)

    __rmul__ = __mul__

    def returnMatrix(self):
        return deepcopy(self.matrixLines)

    def transpose(self):
        size = self.size()
        newList = []
        for i in range(size[1]):
            newList.append([0] * size[0])
        for i in range(size[0]):
            for j in range(size[1]):
                newList[j][i] = self.matrixLines[i][j]
        self.matrixLines = newList
        return Matrix(newList)

    @staticmethod
    def transposed(matrix):
        size = matrix.size()
        newList = []
        for i in range(size[1]):
            newList.append([0] * size[0])
        matrixLines = matrix.returnMatrix()
        for i in range(size[0]):
            for j in range(size[1]):
                newList[j][i] = matrixLines[i][j]
        return Matrix(newList)

    @staticmethod
    def range(matrix):
        matrixLines = matrix.returnMatrix()
        size = matrix.size()

        def findMax(matrixLines, size, j):
            maxEl = 0
            inI = 0
            for i in range(size[0]):
                if abs(matrixLines[i][j]) >= maxEl:
                    maxEl = abs(matrixLines[i][j])
                    inI = i
            if matrixLines[inI][j] != 0:
                return inI
            # Ещё не придумал
        for j in range(size[1]):
            inI = findMax(matrixLines, size, j)


exec(stdin.read())
