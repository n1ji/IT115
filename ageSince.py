from datetime import datetime

specific_date = datetime(2004, 12, 28)
specific_date_1 = datetime(2002, 6, 19)
current_date = datetime.now()
time_difference_1 = current_date - specific_date_1
time_difference = current_date - specific_date
days_since = time_difference.days
days_since_1 = time_difference_1.days

daysOlder = specific_date - specific_date_1
print("\n")
print(f"Time since {specific_date}:")
print(f"{days_since} days since {specific_date}\n")
print(f"Time since {specific_date_1}:")
print(f"{days_since_1} days since {specific_date_1}\n")
print(f"You are {daysOlder.days} days older than them")
print("\n")