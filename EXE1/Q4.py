# Riki Rubin 326380359
# Hadas Donat 325950954

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_twin_prime(n: int):
    if not isinstance(n, int) or not is_prime(n):
        return "invalid input"
    if is_prime(n - 2):
        return n - 2
    if is_prime(n + 2):
        return n + 2
    return "invalid input"

if __name__ == "__main__":
    try:
        n = int(input("enter prime number: "))
        print(get_twin_prime(n))
    except ValueError:
        print("invalid input")
