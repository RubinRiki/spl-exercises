# Riki Rubin 326380359
# Hadas Donat 325950954
# Q5.py — sortedzip using recursion only (no sorted()/sort()), Python 3.8 compatible

from typing import List, Tuple
from tailrecurse import tail_call_optimized


def merge(a: List, b: List) -> List:
    """Recursive merge of two sorted lists (plain recursion)."""
    if not a:
        return b[:]
    if not b:
        return a[:]
    if a[0] <= b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])


def mergesort_recursive(arr: List) -> List:
    """Plain recursive merge sort."""
    n = len(arr)
    if n <= 1:
        return arr[:]
    mid = n // 2
    left = mergesort_recursive(arr[:mid])
    right = mergesort_recursive(arr[mid:])
    return merge(left, right)


def insert_tail(x, sorted_list: List) -> List:
    """Tail-friendly recursive insertion of x into an already-sorted list."""
    if not sorted_list:
        return [x]
    if x <= sorted_list[0]:
        return [x] + sorted_list
    return [sorted_list[0]] + insert_tail(x, sorted_list[1:])


@tail_call_optimized
def insertionsort_tail(arr: List, acc: List = None) -> List:
    """Tail-recursive insertion sort using an accumulator (TCO)."""
    if acc is None:
        acc = []
    if not arr:
        return acc
    return insertionsort_tail(arr[1:], insert_tail(arr[0], acc))


def zip_recursive(*lists: List) -> List[Tuple]:
    """Recursive zip of multiple lists (stops at the shortest length)."""
    if any(len(lst) == 0 for lst in lists):
        return []
    heads = tuple(lst[0] for lst in lists)
    tails = tuple(lst[1:] for lst in lists)
    return [heads] + zip_recursive(*tails)


def sortedzip_recursive(lists: List[List]) -> List[Tuple]:
    """Sort each list via plain-recursive merge sort, then zip recursively."""
    sorted_lists = [mergesort_recursive(lst) for lst in lists]
    return zip_recursive(*sorted_lists)


def sortedzip_tail(lists: List[List]) -> List[Tuple]:
    """Sort each list via tail-recursive insertion sort (TCO), then zip recursively."""
    sorted_lists = [insertionsort_tail(lst) for lst in lists]
    return zip_recursive(*sorted_lists)


if __name__ == "__main__":
    # No loops in printing – each print is explicit
    data = [[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']]

    r1 = sortedzip_recursive(data)
    print("Q5 (recursive):", r1)

    r2 = sortedzip_tail(data)
    print("Q5 (tail):", r2)
