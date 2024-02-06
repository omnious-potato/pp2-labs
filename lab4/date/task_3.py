from datetime import datetime

now = datetime.now()
today = now.replace(microsecond=0)
print(f"Current date: \t\t{today}")