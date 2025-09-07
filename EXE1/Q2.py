# Riki Rubin 326380359
# Hadas Donat 325950954

def sum_digit(num):
    return sum(int(d) for d in str(abs(num)))

if __name__ == "__main__":
    try:
        n = int(input("enter number: "))
        print(sum_digit(n))
    except:
        print("invalid input")
