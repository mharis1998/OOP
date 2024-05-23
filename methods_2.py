## CLass Method:
## ** Accept a cls parameter(refering to the class) instead of self.
## ** Cannot Modify object instance state
## ** Usefull for operators related to the class itself (e.g factory methods)


## Static Method
## **  No access to cls or self
## ** Work like regular functions but belong to the class namespace
## ** Usefull for utility function that don't rely on instance or class static


class Book:
    Types=("Hardcore", "paperback")

    def __init__(self,name,type,weight):
        self.name=name
        self.type=type
        self.weight=weight
    
    @classmethod
    def class_method(cls,name,page_weight):
        return Book(name,Book.Types[0],page_weight+100)
    
    @staticmethod
    def static_method(name,page_weight):
        return Book(name,Book.Types[0],page_weight+100)
    
    def __str__(self) -> str:
        return f"Book {self.name}, {self.type} and weighting {self.weight}"
    

book=Book.class_method("Harry POtter", 1500)
print(book)
book_2=Book.static_method("Harry POtter", 1500)
Book_3=Book("book","soft","212")
# #print(book)
print(book_2)
print(Book_3)