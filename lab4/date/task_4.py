from datetime import datetime, timedelta

def calculate_diff(first:datetime, second:datetime):
    diff = second - first
    return round(diff.total_seconds())



if __name__ == "__main__":
    date_1 = datetime.strptime(input("Enter first date in DD.MM.YYYY: "), "%d.%m.%Y")
    date_2 = datetime.strptime(input("Enter second date in DD.MM.YYYY: "), "%d.%m.%Y")
    print(f"Difference in seconds: {calculate_diff(date_1, date_2)}")

