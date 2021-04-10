from __future__ import annotations
from typing import Any


class Point:
    __slots__ = ('_x', '_y')

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._x = self.__validate(x)
        self._y = self.__validate(y)

    def __validate(self, value: Any) -> float:
        return float(value)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, value: float) -> None:
        self._x = self.__validate(value)

    @y.setter
    def y(self, value: float) -> None:
        self._y = self.__validate(value)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: Point) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError()
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Point) -> bool:
        return not self == other
