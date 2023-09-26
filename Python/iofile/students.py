# with open("students.csv") as file:
#     for names in file:
#         # row = names.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]} house")
#         # We can make it simpler using variables to split the content into two
#         name, house = names.rstrip().split(",")
#         print(f"{name} is in {house}")

# Here, we are creating a list, creating a dictionary and storing the key value pairs and then storing the values in a sorted manner in the list

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
