def square(x): return x**2
def double(x): return 2 * x
def reciprocal(x): return 1/x if x != 0 else None

def apply_funcs(numbers: list, funcs: list) -> dict:
    return {f.__name__: [f(n) for n in numbers] for f in funcs}

if __name__ == "__main__":
    funcs = [square, double, reciprocal]
    nums = [1, 2, 3, 4]
    print("Apply functions:", apply_funcs(nums, funcs))
