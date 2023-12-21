#!/usr/bin/python3

import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n == 1:
        return [1]
    if n % 2 == 0:
        return [2, n // 2]
    
    x = 2
    y = 2
    d = 1
    f = lambda x: (x**2 + 1) % n
    
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    
    if d == n:
        return None
    else:
        return [d, n // d]

def factorize_rsa(number):
    factors = pollard_rho(number)
    if factors is None:
        return "Could not factorize"
    else:
        return f"{number}={'*'.join(map(str, factors))}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    with open(input_file, 'r') as file:
        number = int(file.readline().strip())

    result = factorize_rsa(number)
    print(result)
