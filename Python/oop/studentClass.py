#Classes and Objects - Creating our own datatype

class Student:
    def __init__(self, name, house): #we can use house=None as its default value so that we can make it optional 
        if not name: #if name == "":
            raise ValueError("Missing Value")
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    

    @property
    def house(self): #In getter method, we will always pass only 1 value i.e. self as we know what object we have to get already.
        return self._house #We're using underscore for the instance variable to differentiate between the properties and attributes as we've named both as house. Why _? coz it's identical and python will consider it as we are doing it intentionally. Hence, it is in python convention.
    
    @house.setter
    def house(self, house): #Whereas, In setter method, we have to pass the object as an argument along with self to access the object as we don't know what object we're setting
        if house not in ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]:
            raise ValueError("Invalid house")
        self._house = house
 
def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)

#Bruteforce
# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

#Optimized - We first created variables name and house and then created variable student where we are inserting name and house as an object in the class Student
#Why - It will help us have more control over our correctness of collecting data as user won't be able to pass any value to the class 
def get_student():
    name = input ("Name: ")
    house = input("House: ")

    # student = Student(name, house) #Constructor code - this code constructs a student object for us 
    # return student
    return Student(name, house)

if __name__ == "__main__":
    main()