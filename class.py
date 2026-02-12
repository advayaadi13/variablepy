class student:
    grade = 10
    print("Hi, I am a student of grade", grade)


ob = student()

class student:
    grade = 10
    name = "Penguin"

    def introduction(self):
        print("Hi, I am a student")


    def details(self):
        print("My name is", self.name)
        print("I study in grade", self.grade)


ob = student()
ob.introduction()
ob.details()            



class parrot:
    species = "bird"


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


blu = parrot("Blu", 10)
woo = parrot("Woo", 15)



print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))
print(blu.sing("'Happy'"))
print(blu.dance())