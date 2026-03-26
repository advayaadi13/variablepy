with open("filehandling3.txt", "w")as file:
    file.write("Hi! I am penguin and I am 1yr old")
file.close()

with open("filehandling3.txt", "r") as file:
    data = file.readlines()
    print("Words in the file are.....")
    for line in data:
        word = line.split()
        print(word)
file.close()


new_file = open("new_file.txt", "x")
new_file.close()

import os
print("Checking if my_file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

my_file = open("my_file.txt", "w")
my_file.write("Hi! I am Penguin and I am 1yr old")
my_file.close()

os.remove("filehandling3.txt")

os.rmdimr("Folder")
