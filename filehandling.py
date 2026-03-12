file = open("filehandling.txt", "w")
file.write("\nThis is an application of File Handling in Python")
file.write("\nHello my name is Aadi")
file.write("\nI am 14yrs old")
file.close()

file1 = open("filehandling.txt", "r")
print(file1.read())
file1.close()


file2 = open("filehandling.txt", "a")
file2.write("\nI am from India and I live in New Zealand")
file2.write("\nMy Brother is Ahaan, he is 4yrs old")