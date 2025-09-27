# Riki Rubin 326380359
# Hadas Donat 325950954
# Q4: Check if an integer is a palindrome (no loops).

from tailrecurse import tail_call_optimized


def is_palindrome_recursive(n: int) -> bool:
    """Plain recursion on the string representation."""
    s = str(abs(n))
    def rec(x: str) -> bool:
        if len(x) <= 1:
            return True
        return x[0] == x[-1] and rec(x[1:-1])
    return rec(s)


@tail_call_optimized
def is_palindrome_tail(n: int) -> bool:
    """Tail-recursive two-pointer check on the string representation."""
    s = str(abs(n))
    def rec(i: int, j: int) -> bool:
        if i >= j:
            return True
        if s[i] != s[j]:
            return False
        return rec(i + 1, j - 1)
    return rec(0, len(s) - 1)


if __name__ == "__main__":
    # First: results of the plain recursive version
    print("Recursive:")
    print("123454321 →", is_palindrome_recursive(123454321))
    print("1221      →", is_palindrome_recursive(1221))
    print("10        →", is_palindrome_recursive(10))
    print("7         →", is_palindrome_recursive(7))
    print("12321     →", is_palindrome_recursive(12321))
    print("123       →", is_palindrome_recursive(123))

    # Second: results of the tail-recursive version
    print("\nTail-recursive:")
    print("123454321 →", is_palindrome_tail(123454321))
    print("1221      →", is_palindrome_tail(1221))
    print("10        →", is_palindrome_tail(10))
    print("7         →", is_palindrome_tail(7))
    print("12321     →", is_palindrome_tail(12321))
    print("123       →", is_palindrome_tail(123))