def fibonacci(n):
    """
    Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
    """
    a = 0
    b = 1

    for i in range(0,n):
        c = a+b
        a = b
        b = c
        print(b)

fibonacci(5)
fibonacci(2)
fibonacci(10)