import json
from student import Student

class GradeManager:
    def __init__(self, filename="grades.json"):
        self.filename = filename
        self.students = {}
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for student_data in data.get("students", []):
                    student = Student(
                        id=str(len(self.students) + 1),  # Generate ID
                        name=student_data["name"],
                        grades=student_data["grades"]
                    )
                    self.students[student.id] = student
        except FileNotFoundError:
            self.students = {}
    
    def save_data(self):
        data = {
            "students": [
                {
                    "name": student.name,
                    "grades": student.grades
                }
                for student in self.students.values()
            ]
        }
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    
    def add_student(self, id, name):
        if id not in self.students:
            self.students[id] = Student(id, name)
            self.save_data()
            return True
        return False
    
    def add_grade(self, student_id, subject, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(subject, grade)
            self.save_data()
            return True
        return False
    
    def get_student(self, student_id):
        return self.students.get(student_id)
