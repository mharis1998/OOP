class CLassTest:
    class_var=21
    def instance_method(self):
        print(f"Called instance_method of {self}")
    
    ## Class Method
    @classmethod
    def class_method(cls):
        CLassTest.class_var=3122
        print(f"Called class_method {CLassTest.class_var}")
    
    @staticmethod
    def static_method():
        CLassTest.class_var=3122
        print(f"Static Method {CLassTest.class_var}")
    

CLassTest.static_method()
CLassTest.class_method()
obj=CLassTest()
obj.instance_method()
