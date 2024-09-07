def fibonacci(num):
    if not isinstance(num, int):
        raise TypeError("Input should be an integer.")
    
    a = 0
    b = 1
    for i in range(num):
        yield a
        c = a + b
        a = b
        b = c
try:
    a = fibonacci('fdaf')
    list(a)
except TypeError as err:
    print(err)
