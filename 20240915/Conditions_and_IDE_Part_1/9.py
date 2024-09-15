num_countries = int(input("בכמה מדינות בעולם טיילת? "))

if num_countries == 0:
    print("הכי טוב בארץ")
elif 1 <= num_countries <= 10:
    print("יש 195 מדינות בעולם")
elif num_countries > 10:
    favorite_country = input("מה המדינה שהכי נהנת בה? ")
    print(f"נהדר! {favorite_country} נשמעת מדינה מדהימה!")
