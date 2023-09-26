class Wizard: #Superclass
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name!")
        self.name = name

    ...
    
class Student(Wizard): #Subclass 1
    def __init__(self, name, house):
        super().__init__(name) # To refer to the functionality of the super class Wizard. We can access the functionality and avoid repeating ourselves. Here, super() helps us to refer to the super class Wizard and __init__() helps us to access the functionality of the same super class. 
        self.house = house

    ...

class Professor(Wizard): #Subclass 2
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject