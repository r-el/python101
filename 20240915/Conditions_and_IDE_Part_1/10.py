day_number = int(input("הכנס את מספר היום (1-7): "))

if day_number == 1:
    print("יום ראשון - יום לימודים")
elif day_number == 2:
    print("יום שני - יום לימודים")
elif day_number == 3:
    print("יום שלישי - יום לימודים")
elif day_number == 4:
    print("יום רביעי - יום לימודים")
elif day_number == 5:
    print("יום חמישי - יום לימודים")
elif day_number == 6:
    print("יום שישי - מתכוננים ליום שבת")
elif day_number == 7:
    print("יום שבת - שבת היום")
else:
    print("מספר לא תקין, הכנס מספר בין 1 ל-7")

day_string = input("הכנס את שם היום (ראשון, שני, שלישי, רביעי, חמישי, שישי, שבת): ")

if day_string == "ראשון":
    print("יום ראשון - יום לימודים")
elif day_string == "שני":
    print("יום שני - יום לימודים")
elif day_string == "שלישי":
    print("יום שלישי - יום לימודים")
elif day_string == "רביעי":
    print("יום רביעי - יום לימודים")
elif day_string == "חמישי":
    print("יום חמישי - יום לימודים")
elif day_string == "שישי":
    print("יום שישי - מתכוננים ליום שבת")
elif day_string == "שבת":
    print("יום שבת - שבת היום")
else:
    print("שם יום לא תקין, הכנס שם יום תקין")