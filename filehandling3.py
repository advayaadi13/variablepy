file1 = open('filehandling3.txt', 'r')

file2 = open('filehandlingupdated3.txt', 'w')

for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)




        file2.write(line)


file2.close()
file1.close()        