import numpy as np

from copy import deepcopy
from typing import List, Union, Tuple


class ArithmeticMixin(np.lib.mixins.NDArrayOperatorsMixin):
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        for inp in inputs:
            if not isinstance(inp, type(self)):
                return NotImplemented
        inputs = (inp.data for inp in inputs)
        return type(self)(getattr(ufunc, method)(*inputs, **kwargs))


class GetSetMixin:
    @property
    def shape(self) -> Tuple[int, int]:
        return len(self._data), len(self._data[0])

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


class StringMixin:
    def __str__(self):
        return "\n".join("\t".join(str(val) for val in row) for row in self.data)


class WriteToFileMixin:
    def save(self, filepath: str):
        with open(filepath, "w") as f:
            f.write(str(self))


class HashMixin:
    def __hash__(self):
        return sum([int(sum(row)) for row in self.data]) % (int(1e9) + 7)
