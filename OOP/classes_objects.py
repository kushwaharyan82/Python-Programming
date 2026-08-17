class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"I am studying {self.course}.")


student1 = Student("Aryan", 19, "BTech AI/ML")

student1.introduce()
