#To format user's input

import re

name = input("Enter your name : ")

matches = re.search(r"^(.+), *(.+)$", name) #Used * to handle 1 or more spaces
if matches:
    name = f"{matches.group(2)} {matches.group(1)}"

#Using Walrus Operator to tighten the code
# if matches := re.search(r"^(.+), *(.+)$", name): #Used * to handle 1 or more spaces
#     name = f"{matches.group(2)} {matches.group(1)}"  

print(f"Hello, {name}")    