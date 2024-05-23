## So instead of using average function which know nothing about the student we can class(OOP) student

class student:
    def __init__(self,name="Rolf",grades=[21,31,21,321]) -> None:
        self.name="Rolf"
        self.grades=[1,2,4,5,5]
    def average(self)-> str:
        return sum(self.grades)/len(self.grades)


s=student(grades=[98,78,821,21])
a=s.average()
print(a)
