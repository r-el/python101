is_raining = input("האם יורד בחוץ גשם (yes / no)? ")

if is_raining.lower() in ["yes", "y"]:
    print("לא לשכוח מטרייה.")
elif is_raining.lower() in ["no", "n"]:
    print("לא לקחת מטרייה.")
else:
    print("תשובה לא תקינה, נא לענות ב-yes או no.")