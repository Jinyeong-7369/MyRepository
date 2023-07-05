from Cal import add, sub, mul, div


def test_add() -> None:
    a, b = 1, 2
    result = add(a = a, b = b)
    assert a + b == result, "Error : function 'add'"

def test_sub() -> None:
    a, b = 1, 2
    result = sub(a = a, b = b)
    assert a - b == result, "Error : function 'sub'"

def test_mul() -> None:
    a, b = 1, 2
    result = sub(a = a, b = b)
    assert a * b == result, "Error : function 'mul'"

def test_div() -> None:
    a, b = 1, 2
    result = div(a = a, b = b)
    assert a / b == result, "Error : function 'div'"