DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

num_of_days = int(input("נא הזן מספר ימים: "))

minutes = num_of_days * HOURS_IN_DAY * MINUTES_IN_HOUR
seconds = num_of_days * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
percentage = (num_of_days / DAYS_IN_YEAR) * 100

print("כמות הדקות בימים הנ\"ל:", minutes)
print("כמות השניות בימים הנ\"ל:", seconds)
print("אחוז הימים הנ\"ל מתוך שנה שלמה:", percentage)