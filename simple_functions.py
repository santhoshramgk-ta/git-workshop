# Custom python functions


def double_number(a):
    """
     Doubles the value of the input number and prints the value before and after doubling.

    Parameters:
    a (int or float): The number to be doubled.

    Returns:
    None: This function prints the result but does not return any value.
    
    Example:
    >>> double_number(4)
    value before double_number(): 4
    value after double_number(): 8
    """
    print(f"value before double_number(): {a}")
    result = a + a
    print(f"value after double_number(): {result}")
    return 0

def square_number(a):
    """
    Squares the value of the input number and prints the value before and after squaring.

    Parameters:
    a (int or float): The number to be squared.

    Returns:
    None: This function prints the result but does not return any value.

    Example:
    >>> square_number(4)
    value before square_number(): 4
    value after square_number(): 16
    """
    print(f"value before square_number(): {a}")
    result = a * a
    print(f"value after square_number(): {result}")
    return 0