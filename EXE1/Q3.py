gematria = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6,
    'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30,
    'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
    'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
}

def get_gematria(word: str) -> int:
    return sum(gematria.get(ch, 0) for ch in word)

if __name__ == "__main__":
    try:
        s = input().strip()
        print(get_gematria(s))
    except Exception:
        print("invalid input")

if __name__ == "__main__":
    print('Gematria of "שלום" =', get_gematria("שלום"))
