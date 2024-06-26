ONE = 1
PI = 3.14159265358979323846
E = 2.718281828459045
R = 8.31446261815324
FI = 1.61803398874989484820 # Pi/2
def occurance(itt: object) -> dict:
    """Count the occurance of each element in an itterable element f.e. letters, numbers in an array or string.

    Args:
        itt (Itterable): Itterable element to count the occurance of.

    Returns:
        dict {element : count}: Output with all counted occurances of each element.

    """
    out = {}
    for occ in itt:
        if occ in out:
            out[occ] += 1
        else:
            out[occ] = 1
    return out

def isprime(n:int) -> bool:
    """Returns True if n is prime.

    Args:
        n (int): Any number.

    Returns:
        bool: If n is a prime number, return True, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if not n % 2:
        return False
    if not n % 3:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if not n % i:
            return False

        i += w
        w = 6 - w

    return True

def sumdigit(number) -> int:
    """Sums the digits of a number.

    Args:
        number (ConvertableToString): A parameter that can be converted to a string, preferably an int.


    Returns:
        int: the sum of the digits of the number.
    """
    out = 0
    for digit in str(number):
        out += int(digit)
    return out

def triangleCheck(a, b, c) -> bool:
    """If the sum of the two smallest sides is greater than the largest side, then the triangle is valid.

    Args:
        a, b, c (int | float): The sides of the triangle. If negative, the absolute value is given.


    Returns:
        bool: True if the triangle is valid, False otherwise.

    """
    sides = abs(a), abs(b), abs(c)
    return sum(sides) - max(sides) * 2 > 0

def ifpythagorean(a, b, c) -> bool:
    """If the triangle is a right triangle, then it is a pythagorean triangle.

    Args:
        a, b, c (int | float): The sides of the triangle. Can be negative.


    Returns:
        bool: True if the triangle is a right triangle. False otherwise.
    """
    sides = a*a, b*b, c*c
    return not sum(sides) - max(sides) * 2

def printarray(array:list):
    """Prints a 2d array. right adjusting the objects for the space difference between object sizes.

    Args:
        twod (list): array for printing
    """
    maxlength = 0
    for line in array:
        for object in line:
            if maxlength < len(str(object)):
                maxlength = len(str(object))
    for line in array:
        for object in line:
            print(str(object).rjust(maxlength), end=" ")
        print()

        