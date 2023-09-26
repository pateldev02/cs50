import re

url = input("Username : ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# print(f"Username is : {username}")

# Using re.search to handle other web domains and looking for a particular O/P

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username is : {matches.group(1)}")

