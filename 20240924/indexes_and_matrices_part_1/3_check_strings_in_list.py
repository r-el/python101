languages = ["Python", "Java", "Javascript", "C", "C++", "C#", "HTML",
             "CSS", "Go", "Typescript", "NodeJS", "Django", "React",
             "Vue", "Git", "Github", "Linux", "NextJS", "Netlify"]

# הדפסת האינדקסים של Vue, CSS, Netlify, Go, Java
specified_languages = ["Vue", "CSS", "Netlify", "Go", "Java"]
indices = {lang: languages.index(lang) for lang in specified_languages}
print("Indices of specified languages:", indices)

# בדיקה האם המחרוזות קיימות במערך והדפסת המיקום שלהן במידה וקיימות
strings_to_check = ["GITHUB", "Github", "git", "Vue", "Css"]
print("\n".join([f"{string} found at index {languages.index(string)}" if string in languages else f"{string} not found in the list" for string in strings_to_check]))
