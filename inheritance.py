class Device:
    def __init__(self,name,connected_by):
        self.name=name
        self.connected_by=connected_by
        self.connected=True

    def __str__(self) -> str:
        return f"Devica name is {self.name}, connection {self.connected_by}"
    
    def disconnected(self):
        self.connected=False
        print("Disconnected")

class printer(Device):
    def __init__(self, name, connected_by,capacity):
        super().__init__(name, connected_by)
        self.capacity=capacity
        self.remaining_pages=capacity

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)" 
    
    def print(self,pages):
        if not self.connected:
            print("Your printer is not connected")
        else:
            print(f"Printing {pages} pages")
            self.remaining_pages-=pages


prit=printer("P1","USB",1500)
print(prit.capacity)
prit.print(500)
print(prit.remaining_pages)