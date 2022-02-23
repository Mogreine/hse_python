from copy import deepcopy
from typing import List, Union

from hw3.mixins import ArithmeticMixin, GetSetMixin, WriteToFileMixin, StringMixin, HashMixin


class Matrix(HashMixin, ArithmeticMixin, GetSetMixin, WriteToFileMixin, StringMixin,):
    _mul_hash = {}

    def __init__(self, data: List[List[Union[int, float]]]):
        row_lens = [len(row) for row in data]
        assert min(row_lens) == max(row_lens), "All the rows must have the same length."
        self._data = deepcopy(data)

    @classmethod
    def from_file(cls, filepath: str):
        with open(filepath, "r") as f:
            res = f.readlines()

        res = [list(map(lambda num: float(num), line.split("\t"))) for line in res]

        return cls(res)

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

        key = self.__hash__(), other.__hash__()
        if key in self._mul_hash:
            return self._mul_hash[key]

        res = [[0] * self.shape[0] for _ in range(other.shape[1])]
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                res[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.shape[1]))

        self._mul_hash[key] = Matrix(res)

        return Matrix(res)
