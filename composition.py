## Inheritance models an "is-a" relationship.
## Composion models an "has-a" relationship.

class Engine:
    def __init__(self,type,n_pistons):
        self.type=type
        self.n_pistons=n_pistons
    def __str__(self) -> str:
        return f"Engine type {self.type} and number of pistions is {self.n_pistons}"
    
class wheel:
    def __init__(self,type):
        self.type=type
    def __str__(self) -> str:
        return f"Wheel TYpe {self.type}"

class Car:
    def __init__(self,name,Model,Engine,wheel):
        self.name=name
        self.Model=Model
        self.Engine=Engine
        self.wheel=wheel

    def __str__(self) -> str:
        return f"Car {self.name}, {self.Model}, {self.Engine}, {self.wheel}"


Engine1=Engine("Diesel",6)
wh1=wheel("All season")
car1=Car("Honda","Santa fe",Engine1,wh1)
print(car1)
print(car1.Engine)