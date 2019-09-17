
class Junior:
    def total(self):
        print("totally 15 juniors")

class Senior:
    def total(self):
        print("totally 20 seniors")

class Student:
    def check(self, section):
        section.total()

sec1 = Junior()
sec2 = Senior()
s1 = Student()
s1.check(sec1)
s1.check(sec2)