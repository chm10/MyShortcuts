# !usr/bin/env python3

def gerar_finito_fibo(repetir):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

def gerar_infinito_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    ## Result from finite 
""" 
    generator = (n for n in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
    for f in generator:
        print(f) 
"""

    ## Result from finite
""" 
    generator = gerar_finito_fibo(100)
    for f in generator:
        print(f) 
"""

    ## Result from infinite
""" 
generator = gerar_infinito_fibo()
while True:
    print(next(f))
"""



