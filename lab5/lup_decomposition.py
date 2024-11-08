# lup_decomposition.py

class Matrix:
    def __init__(self, data):
        self.data = data  # Двовимірний список (матриця)
        self.n = len(data)

    def __add__(self, other):
        result = []
        for i in range(self.n):
            row = [self.data[i][j] + other.data[i][j] for j in range(self.n)]
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        result = []
        for i in range(self.n):
            row = [self.data[i][j] - other.data[i][j] for j in range(self.n)]
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            # Множення матриць
            result = []
            for i in range(self.n):
                row = []
                for j in range(self.n):
                    sum_elem = sum(self.data[i][k] * other.data[k][j] for k in range(self.n))
                    row.append(sum_elem)
                result.append(row)
            return Matrix(result)
        elif isinstance(other, list):
            # Множення матриці на вектор
            result = []
            for i in range(self.n):
                sum_elem = sum(self.data[i][j] * other[j] for j in range(self.n))
                result.append(sum_elem)
            return result  # Повертаємо вектор
        else:
            raise ValueError("Unsupported operand for multiplication")

    def transpose(self):
        transposed_data = []
        for i in range(self.n):
            row = [self.data[j][i] for j in range(self.n)]
            transposed_data.append(row)
        return Matrix(transposed_data)

def lup_decomposition(A):
    n = len(A)
    # Ініціалізація матриці перестановок
    P = list(range(n))
    A = [row[:] for row in A]  # Копія матриці A

    for k in range(n):
        # Знаходимо максимальний елемент у стовпці для перестановки
        pivot = max(range(k, n), key=lambda i: abs(A[i][k]))
        if abs(A[pivot][k]) < 1e-12:
            raise ValueError("Matrix is singular!")
        # Перестановка рядків
        A[k], A[pivot] = A[pivot], A[k]
        P[k], P[pivot] = P[pivot], P[k]
        for i in range(k+1, n):
            A[i][k] /= A[k][k]
            for j in range(k+1, n):
                A[i][j] -= A[i][k] * A[k][j]

    # Витягуємо L і U з A
    L = [[0 if i != j and i < j else (1 if i == j else A[i][j]) for j in range(n)] for i in range(n)]
    U = [[A[i][j] if i <= j else 0 for j in range(n)] for i in range(n)]

    return L, U, P

def lup_solve(L, U, P, b):
    n = len(L)
    # Застосовуємо перестановку до вектора b
    Pb = [b[P[i]] for i in range(n)]

    # Прямий хід (L y = Pb)
    y = [0]*n
    for i in range(n):
        y[i] = Pb[i] - sum(L[i][j]*y[j] for j in range(i))

    # Зворотний хід (U x = y)
    x = [0]*n
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(U[i][j]*x[j] for j in range(i+1, n))) / U[i][i]

    return x
