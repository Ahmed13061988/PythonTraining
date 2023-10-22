import re

string = "Hello! My name is Ahmed."


var = re.search(r"Hello", string)

if re.search(r"Air", "airline") != None:
    print("Pattern found")
else:
    print("Pattern not found")
