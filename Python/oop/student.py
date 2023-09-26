#Tuple - Immutable datatype
# For Tuples, we use () paranthesis whereas for Lists, we use [].

#Tuple

# def main():
#     student = get_student()

# #Writing these two lines to check how tuple is immutable.
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw" #We're using "=" as we are assigning a value and not comparing it 
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")

#     return (name, house) #Tuple

# if __name__ == "__main__":
#     main()

#O/P for this codebase where we are using Tuple and updating the value for Padma's house to Ravenclaw
# Name: Padma      
# House: Gryffindor
# Traceback (most recent call last):
#   File "E:\Web Dev\Python\CS50\oop\student.py", line 19, in <module>
#     main()
#   File "E:\Web Dev\Python\CS50\oop\student.py", line 9, in main
#     student[1] = "Ravenclaw" #We're using "=" as we are assigning a value and not comparing it
#     ~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment



#As we were using tuple which is an immutable data structure, if we had to update a value we definetly would've get an TypeError as ofcourse it is immutable. Here, I am writing a code where I am replacing the tuple with a list to see if we can update or replace a value or not.


#List

def main():
    student = get_student()

#Writing these two lines to check how tuple is immutable and list is not.
    if student[0] == "Padma":
        student[1] = "Ravenclaw"


    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")

    return [name, house] #Not Tuple but a list

if __name__ == "__main__":
    main()

#O/P for this codebase where we are using list
# Name: Padma      
# House: Gryffindor 
# Padma from Ravenclaw


#Dictionary

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f'{student["name"]} from {student["house"]}')

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()\
    
#O/P
# Name: Padma
# House: Gryffindor
# Padma from Ravenclaw


