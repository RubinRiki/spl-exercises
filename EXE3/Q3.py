# Riki Rubin 326380359
# Hadas Donat 325950954
# Q3: Compute LCM(a, b) without loops.

from tailrecurse import tail_call_optimized


def gcd_recursive(a: int, b: int) -> int:
    """Plain recursive Euclidean GCD."""
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


@tail_call_optimized
def gcd_tail(a: int, b: int) -> int:
    """Tail-recursive Euclidean GCD."""
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_tail(b, a % b)


def lcm_via_gcd_recursive(a: int, b: int) -> int:
    """LCM computed with plain-recursive GCD."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd_recursive(a, b)


def lcm_via_gcd_tail(a: int, b: int) -> int:
    """LCM computed with tail-recursive GCD."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd_tail(a, b)


if __name__ == "__main__":
    #print("Q3:", lcm_via_gcd_recursive(4, 6))  # 12 12
    print("Q3:", lcm_via_gcd_tail(4, 6))  # 12 12
