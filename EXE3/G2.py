# Riki Rubin 326380359
# Hadas Donat 325950954
# G2.py — Infinite prime generator (each next() yields the next prime)

import math


def primes():
    """Yield primes in increasing order using incremental trial division."""
    found = []            # previously found primes for trial division
    n = 2
    while True:
        is_prime = True
        limit = int(math.isqrt(n))
        for p in found:
            if p > limit:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            found.append(n)
            yield n
        n += 1


if __name__ == "__main__":
    g = primes()
    # print first 10 primes (explicit, no loops required by the assignment here)
    p1 = next(g); print("Prime:", p1)
    p2 = next(g); print("Prime:", p2)
    p3 = next(g); print("Prime:", p3)
    p4 = next(g); print("Prime:", p4)
    p5 = next(g); print("Prime:", p5)
    p6 = next(g); print("Prime:", p6)
    p7 = next(g); print("Prime:", p7)
    p8 = next(g); print("Prime:", p8)
    p9 = next(g); print("Prime:", p9)
    p10 = next(g); print("Prime:", p10)
