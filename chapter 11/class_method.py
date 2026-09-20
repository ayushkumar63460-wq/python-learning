# allows operations releated to class itself,
# take (cls) as the first parameter which represents the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

        Student.count += 1
        Student.total_gpa +=1

#INSTANCE METHOD:
    def get_info(self):
        return f"{self.name} {self.gpa}"

#CLASS METHOD:
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}" 



s1= Student("John", 3.4)
s2 = Student("Max", 4.2)
s3 = Student("Vik", 5.0)

print(Student.get_count())

 

