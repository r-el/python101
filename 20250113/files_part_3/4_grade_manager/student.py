class Student:
    def __init__(self, id, name, grades=None):
        self.id = id
        self.name = name
        self.grades = grades if grades else {}
    
    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)
    
    def get_average(self, subject=None):
        if subject:
            grades = self.grades.get(subject, [])
            return sum(grades) / len(grades) if grades else 0
        
        if not self.grades:
            return 0
            
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def get_subject_grades(self, subject):
        return self.grades.get(subject, [])
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'grades': self.grades
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['name'], data['grades'])
