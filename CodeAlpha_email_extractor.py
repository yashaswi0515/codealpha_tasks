import re

file = open("input.txt", "r")
text = file.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

output = open("emails.txt", "w")

for email in emails:
    output.write(email + "\n")

print("Emails extracted successfully!")