## Person CLass

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
## The str method is called when you wanna turn the object into string
    def __str__(self) -> str:
       return f"Person name: {self.name} and age: {self.age}"
## The repr method is an umbiguous representation of an object
    def __repr__(self) -> str:
        return f"<Persame: {self.name} and age: {self.age}>"

bob=Person("Bob",35)
print(bob)