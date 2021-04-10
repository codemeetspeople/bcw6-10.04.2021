import pytest

from point.point import Point


def test_point_default_constructor():
    p = Point()

    assert p.x == 0.0
    assert p.y == 0.0


def test_point_constructor():
    p = Point(10, 12.3)

    assert p.x == 10.0
    assert p.y == 12.3


def test_point_setters():
    p = Point()

    assert p.x == 0.0
    assert p.y == 0.0

    p.x = 10
    p.y = 22

    assert p.x == 10.0
    assert p.y == 22.0


def test_point_to_string():
    p = Point()

    assert str(p) == '(0.0, 0.0)'


def test_operators():
    p1 = Point()
    p2 = Point()
    p3 = Point(1, 10)

    assert p1 == p2
    assert not p1 != p2

    assert p1 != p3
    assert not p1 == p3


def test_operators_exception():
    class Test:
        pass

    p = Point()

    with pytest.raises(TypeError):
        assert p == Test()
