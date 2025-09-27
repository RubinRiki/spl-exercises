# Riki Rubin 326380359
# Hadas Donat 325950954
# Q2: Sum elements of a tuple without loops.

from tailrecurse import tail_call_optimized
from Q1 import make_tuple_tail

def sum_tuple_recursive(t: tuple) -> int:
    """Plain recursive sum over a tuple."""
    if not t:
        return 0
    return t[0] + sum_tuple_recursive(t[1:])


@tail_call_optimized
def sum_tuple_tail(t: tuple, acc: int = 0) -> int:
    """Tail-recursive sum over a tuple using an accumulator."""
    if not t:
        return acc
    return sum_tuple_tail(t[1:], acc + t[0])


if __name__ == "__main__":
    data = make_tuple_tail(1000)
    #s1 = sum_tuple_recursive(data)
    s2 = sum_tuple_tail(data)
    #print("Q2 s1:", s1)
    print("Q2 s2: ",  s2)
    #assert s1 == s2 == 1000 * 1001 // 2
