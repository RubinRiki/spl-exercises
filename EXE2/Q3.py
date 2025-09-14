# Riki Rubin 326380359
# Hadas Donat 325950954

from datetime import datetime, timedelta

def date_skip(start_date: str, step: int) -> list:
    start = datetime.strptime(start_date, "%d/%m/%Y")
    return [(start + timedelta(days=i*step)).strftime("%d/%m/%Y") for i in range(5)]



if __name__ == "__main__":
    print("Dates skip:", date_skip("01/01/2025", 7))

