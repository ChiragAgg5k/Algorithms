def gcd_iter(a: int, b: int) -> int:
    """A function to calculate the greatest common divisor of two numbers.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The greatest common divisor of a and b.
    """
    
    if a>b:
        smaller = b
    else:
        smaller = a
        
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
    
    return gcd

def gcd_rec(a: int, b: int) -> int:
    """A recursive function to calculate the greatest common divisor of two numbers.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The greatest common divisor of a and b.
    """
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)

def gcd_euclid(a: int, b: int) -> int:
    """GCD using Euclid's algorithm.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The greatest common divisor of a and b.
    """
    
    while b:
        a, b = b, a % b
    
    return a

if __name__ == "__main__":
    print(gcd_iter(12, 17))
    print(gcd_rec(12, 17))
    print(gcd_euclid(100, 5))