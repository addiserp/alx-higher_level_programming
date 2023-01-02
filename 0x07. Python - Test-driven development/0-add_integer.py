def add_integer(a, b=98):
    """ test driven test by adding two numbers
    Args:
        a: test par 1
        b: test par 2
    Returns:
        The result of the two samples a & b
    Raises:
        TypeError: either of them aren't integer or float numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
