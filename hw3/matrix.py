from hw3.mixins import ArithmeticMixin, GetSetMixin, WriteToFileMixin, StringMixin


class Matrix(ArithmeticMixin, GetSetMixin, WriteToFileMixin, StringMixin):
    def __add__(self, other: "Matrix") -> "Matrix":
        assert self.shape == other.shape, "Shape mismatch."

        n, m = self.shape
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(m)] for i in range(n)])

    def __mul__(self, other: "Matrix") -> "Matrix":
        assert self.shape == other.shape, "Shape mismatch."

        n, m = self.shape
        return Matrix([[self.data[i][j] * other.data[i][j] for j in range(m)] for i in range(n)])

    def __matmul__(self, other: "Matrix") -> "Matrix":
        assert self.shape[1] == other.shape[0], "Shape mismatch."

        res = [[0] * self.shape[0] for _ in range(other.shape[1])]
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                res[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.shape[1]))

        return Matrix(res)
