import math 
import decimal

def pi_calculate(n):
    """
    Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
    """
    print(f"%.{n}f" % math.pi)


pi_calculate(2)
pi_calculate(15)
pi_calculate(40)
pi_calculate(4)

def e_calculate(n):
    """
    Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
    """
    print(f"%.{n}f" % math.e)

e_calculate(2)
e_calculate(15)
e_calculate(40)
e_calculate(4)