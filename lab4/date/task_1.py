from datetime import datetime, timedelta

now = datetime.now()
today = now.strftime("%d.%m.%Y")
print(f"Current date: \t\t{today}")

print(f"Date five days ago: \t{(now - timedelta(days=5)).strftime('%d.%m.%Y')}")