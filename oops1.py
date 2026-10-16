class person:
    def __init__(self, name ):
        self.name = name
        
    def display(self):
        print(f"Name: {self.name}")
class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class student(person, person1):
    def __init__(self, name, age, student_id):
        person.__init__(self, name)
        person1.__init__(self, name, age)
        self.student_id = student_id
        
    def display(self):
        person.display(self)
        person1.display(self)
        print(f"Student ID: {self.student_id}")
s1 = student("Charlie", 22, "S001")
s1.display()

