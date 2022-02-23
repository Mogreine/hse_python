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
    def __init__(self, data: List[List[Union[int, float]]]):
        row_lens = [len(row) for row in data]
        assert min(row_lens) == max(row_lens), "All the rows must have the same length."
        self._data = deepcopy(data)

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
