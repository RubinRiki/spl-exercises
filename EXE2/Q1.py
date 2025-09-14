# Riki Rubin 326380359
# Hadas Donat 325950954

from functools import reduce
import time

linear = lambda x: x / 2 + 2
nums = list(range(10001))

# map linear function
linear_list = list(map(linear, nums))

# sum with built-in
sum_builtin = sum(linear_list)

# sum with loop
def sum_loop(vals):
    s = 0
    for v in vals:
        s += v
    return s

sum_imperative = sum_loop(linear_list)

# sum with single HOF
sum_single_hof = reduce(lambda acc, x: acc + (x / 2 + 2), nums, 0)

# measure runtime
def best_time(fn, *args, repeats=5):
    best = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn(*args)
        dt = time.perf_counter() - t0
        if dt < best:
            best = dt
    return best

time_loop = best_time(sum_loop, linear_list)
time_hof  = best_time(lambda vs: reduce(lambda acc, x: acc + (x / 2 + 2), vs, 0), nums)

if __name__ == "__main__":
    print("Sum with sum(map(linear, nums)):", sum_builtin)
    print("Sum with loop:", sum_imperative)
    print("Sum with single HOF:", sum_single_hof)
    print(f"Timing (loop): {time_loop:.6f} sec")
    print(f"Timing (HOF):  {time_hof:.6f} sec")
