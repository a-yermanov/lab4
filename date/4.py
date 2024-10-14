from datetime import datetime

x = datetime.now()
y = datetime(2024, 9, 13)

difference = x - y
sec = difference.total_seconds()
print(sec)