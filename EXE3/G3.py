# Riki Rubin 326380359
# Hadas Donat 325950954
# G3.py — Taylor series for e^x: each next() yields the next partial sum
# e^x = sum_{k=0}^{∞} x^k / k!


def taylor_exp(x: float):
    """Yield successive partial sums of the Taylor series for e^x."""
    k = 0
    term = 1.0   # x^0 / 0!
    acc = 0.0
    while True:
        acc += term
        yield acc
        k += 1
        term *= x / k  # term_k = term_{k-1} * (x / k)


if __name__ == "__main__":
    g = taylor_exp(2.0)  # example for e^2
    # print first 8 partial sums explicitly (no loop if you prefer)
    print(next(g))  # 1.0
    print(next(g))  # 3.0
    print(next(g))  # 5.0
    print(next(g))  # 6.333333333333333
    print(next(g))  # 7.0
    print(next(g))  # 7.266666666666667
    print(next(g))  # 7.355555555555555
    print(next(g))  # 7.380952380952381 (approx)
