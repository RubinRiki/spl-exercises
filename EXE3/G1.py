# Riki Rubin 326380359
# Hadas Donat 325950954
# G1.py — Eager vs. Lazy sequence 0..10000 (time/memory + first 5000)

import sys
import time
import itertools


def build_eager(n: int):
    """Eagerly build tuple(0..n) in memory."""
    return tuple(range(n + 1))


def build_lazy(n: int):
    """Return a generator that yields 0..n lazily (on demand)."""
    def gen():
        i = 0
        while i <= n:
            yield i
            i += 1
    return gen()


def measure(build_fn, n: int):
    """Measure construction time and object size."""
    t0 = time.perf_counter()
    obj = build_fn(n)
    t1 = time.perf_counter()
    return obj, (t1 - t0), sys.getsizeof(obj), type(obj)


if __name__ == "__main__":
    N = 10000

    eager_obj, eager_time, eager_size, eager_type = measure(build_eager, N)
    lazy_obj,  lazy_time,  lazy_size,  lazy_type  = measure(build_lazy,  N)

    # Take first 5000 (actually 0..5000 => 5001 items)
    first_5000_eager = eager_obj[:5001]
    first_5000_lazy  = tuple(itertools.islice(lazy_obj, 5001))

    print("EAGER:", eager_type, "| time:", round(eager_time, 6),
          "| size(bytes):", eager_size, "| len:", len(eager_obj))
    print("LAZY :", lazy_type,  "| time:", round(lazy_time, 6),
          "| size(bytes):", lazy_size,  "| len:", None)  # generator has no length

    print("First 5000 types equal?",
          type(first_5000_eager) == type(first_5000_lazy),
          "| type:", type(first_5000_eager))
    print("First 5000 lengths:", len(first_5000_eager), len(first_5000_lazy))
