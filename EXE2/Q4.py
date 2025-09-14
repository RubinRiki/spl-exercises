# Riki Rubin 326380359
# Hadas Donat 325950954

import math

def power_function(base):
    def inner(exp):
        return exp ** base
    return inner

def powers_list(n, base):
    return map(lambda i: base ** i, range(n))

def exp_taylor(x, terms=10):
    return sum(map(lambda k: (x**k)/math.factorial(k), range(terms)))


if __name__ == "__main__":
    n = int(input("Enter number of powers:\n"))
    base = int(input("Enter base:\n"))
    result = powers_list(n, base)
    print(type(result))
    print(tuple(result))


