answer = input("האם אתה רעב? (כן/לא): ").strip().lower() # .strip() מסיר רווחים מתחילת וסופו של המחרוזת

if answer == "כן":
    print("תכין או תזמין אוכל.")
elif answer == "לא":
    print("נצל את הזמן שלך בחוכמה.")
else:
    print("אנא ענה 'כן' או 'לא'.")