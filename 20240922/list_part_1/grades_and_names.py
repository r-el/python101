# .1 יש ליצור רשימה ריקה בשם grades.
grades = []

# 2 יש להדפיס את אורך הרשימה
print(len(grades))

# 3 יש להוסיף לרשימה grades חמישה ציונים מסוג float.
grades.append(90.5)
grades.append(85.5)
grades.append(80.5)
grades.append(75.5)
grades.append(70.5)
# Or using list concatenation:
# grades += [90.5, 85.5, 80.5, 75.5, 70.5]

# 4 יש להדפיס את כל הציונים הנמצאים ברשימה לפי אינדקסים.
print(grades[0], grades[1], grades[2], grades[3], grades[4])

# 5 יש להחליף את הציונים במיקום הראשון ובמיקום האחרון ולהדפיס מחדש את כל הציונים לפי אינדקסים.
grades[0], grades[-1] = grades[-1], grades[0]
print(grades[0], grades[1], grades[2], grades[3], grades[4])

# 6 יש ליצור רשימה בשם names עם 5 שמות של אנשים.
names = ["Ariel", "Yoni", "Michal", "Shira", "Nava"]

# 7 יש ליצור רשימה בשם grades_and_names ולהכניס לה בתור איברים את רשימת השמות ואת רשימת הציונים.
grades_and_names = [names, grades]
# print(grades_and_names)

# 8 יש להדפיס את גודל הרשימה grades_and_names
print("len of grades_and_names:", len(grades_and_names))

# 9 יש להדפיס את גודל האיבר הראשון ברשימה grades_and_names
print("len of the first element in grades_and_names:", len(grades_and_names[0]))

# 10 יש להדפיס את השם במיקום הראשון עם הציון במיקום הראשון )ולהמשיך עד המיקום האחרון
for i in range(len(grades_and_names[0])):
    print(grades_and_names[0][i], grades_and_names[1][i])
# In one line:
# print("\n".join([f"{name} {grade}" for name, grade in zip(grades_and_names[0], grades_and_names[1])]))

# 11 יש ליצור רשימה חדשה בשם name_last ולמלא אותם בערכים מתאימים, להוסיף אותה לרשימה grades_and_names, להדפיס את אורך הרשימה grades_and_names ולהדפיס את האיבר השלישי שלה.
name_last = ["cohen", "levi", "mizrachi", "peretz", "biton"]
grades_and_names.append(name_last)
print("len of grades_and_names:", len(grades_and_names))
print(grades_and_names[2])
