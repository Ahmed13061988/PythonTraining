# Syntax of opening files.
# file_object = open(file_name_path [, access_mode])
# file_name_path is the filename or path of the file to be opened.
# access_mode is the mode in which the file has to be opened which is optional. If not specified, default value will be read.
# file_object is the object returned by open method which is used for further file operations.
# Example :
# fhr=open("data.txt","r")
# Syntax: for file closing
# file_object.close()

data = open('data.txt', 'r')
line1 = data.readline()
print(line1)
line2 = data.readline()
print(line2)
line3 = data.readline()
print(line3)
all_lines = data.readlines()
print(all_lines)
