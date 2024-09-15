number = int(input("הכנס מספר בין 1 למיליון: "))

if number < 1 or number > 1000000:
    print("הכנסת קלט לא תקין.")
elif number < 500000:
    print("זה מספר קטן.")
elif number < 750000:
    print("זה מספר בינוני.")
else:
    print("זה מספר גדול.")