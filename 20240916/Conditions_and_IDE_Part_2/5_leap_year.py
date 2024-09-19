years = [2000, 2001, 2004, 1900, 2100, 2400]

for year in years:
    # שלב א
    if year % 4 == 0:
        # שלב ב
        if year % 100 == 0:
            # שלב ג
            if year % 400 == 0:
                # שלב ד
                is_leap = True
            else:
                # שלב ה
                is_leap = False
        else:
            # שלב ד
            is_leap = True
    else:
        # שלב ה
        is_leap = False
    print(f"Year {year} is a leap year: {is_leap}")

print("\nUsing single condition:")

for year in years:
    # שלב א
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        is_leap = True
    else:
        is_leap = False
    print(f"Year {year} is a leap year: {is_leap}")
