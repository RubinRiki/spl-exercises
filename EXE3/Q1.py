# Riki Rubin 326380359
# Hadas Donat 325950954
# Q1: Build a tuple of numbers 1..n without loops.

from tailrecurse import tail_call_optimized


def make_tuple_recursive(n: int) -> tuple:
    """Plain recursive construction of tuple(1..n)."""
    if n <= 0:
        return tuple()
    return make_tuple_recursive(n - 1) + (n,)


@tail_call_optimized
def make_tuple_tail(n: int, acc: tuple = tuple()) -> tuple:
    """Tail-recursive construction of tuple(1..n) using an accumulator."""
    if n <= 0:
        return acc
    return make_tuple_tail(n - 1, acc + (n,))


if __name__ == "__main__":
   # t1 = make_tuple_recursive(1000)
    t2 = make_tuple_tail(1000)
   # print("Q1:", len(t1), t1[:5], "...", t1[-5:])
    print("Q1 (tail):", len(t2), t2[:5], "...", t2[-5:])
