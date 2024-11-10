names = ["Ariel", "Yoni", "Michael", "David", "Shlomo"]
birth_years = (1990, 2000, 1995, 1998, 2004)
birth_countries = ("Israel", "USA", "Canada", "UK", "Australia")

for person_details in zip(names, birth_years, birth_countries):
    print(f"Name: {person_details[0]}, Birth Year: {person_details[1]}, Birth Country: {person_details[2]}")