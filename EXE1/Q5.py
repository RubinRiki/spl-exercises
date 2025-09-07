def add_3_dicts(d1: dict, d2: dict, d3: dict) -> dict:
    result = {}
    for key in set(d1) | set(d2) | set(d3):
        values = set()
        for d in (d1, d2, d3):
            if key in d:
                values.add(d[key])
        result[key] = tuple(values)
    return result

if __name__ == "__main__":
    d1 = {'a': 1}
    d2 = {'a': 2, 'b': 3}
    d3 = {'b': 3, 'c': 4}
    print("Merged dictionaries:", add_3_dicts(d1, d2, d3))
