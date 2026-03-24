import pytest

def square(x):
    return x * x

def cube(x):
    return x * x * x

def test_square():
    assert square(2) == 4, "Expected square of 2 to be 4"
    assert square(-3) == 9, "Expected square of -3 to be 9"
    assert square(0) == 0, "Expected square of 0 to be 0"

def test_cube():
    assert cube(2) == 8, "Expected cube of 2 to be 8"
    assert cube(-3) == -27, "Expected cube of -3 to be -27"
    assert cube(0) == 0, "Expected cube of 0 to be 0"

def test_number():
    pytest.raises(TypeError, square, "a string")
    pytest.raises(TypeError, cube, "a string")