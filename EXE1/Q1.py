def get_penta_num(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        return "invalid input"
    return n * (3 * n - 1) // 2

def pentaNumRange(n1: int, n2: int) -> list:
    if not (isinstance(n1, int) and isinstance(n2, int)) or n1 <= 0 or n2 < n1:
        return "invalid input"
    return [get_penta_num(i) for i in range(n1, n2 + 1)]

if __name__ == "__main__":
    print("Pentagonal numbers between 1 and 5:", pentaNumRange(1, 5))

