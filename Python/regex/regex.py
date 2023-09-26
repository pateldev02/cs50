import re

#1 Bruteforce

# email = input("Enter your email : ")

# if "@" and "." in email:
#     print("valid")
# else:
#     print("invalid")

#2 using str functions

# email = input("Enter your email : ").strip()

# name, domain = email.split("@")

#1
# if name and "." in domain:
#     print("Valid")
# else:
#     print("invalid")

#2
# if name and domain.endswith(".edu"):
#     print("valid")
# else:
#     print("invalid")

#3 using re module

email = input("Enter your email : ").strip()

# if re.search(r"^[a-zA-z0-9_]+@[a-zA-Z0-9_]+\.edu$",email): #Here r"stringContent" means a raw string || using backslash as an escape sequence
#     print("valid")  
# else:
#     print("invalid")

if re.search(r"^[a-zA-z0-9_]+@[a-zA-Z0-9_]+\.edu$",email, re.IGNORECASE): #Here r"stringContent" means a raw string || using backslash as an escape sequence
    print("valid")  
else:
    print("invalid")