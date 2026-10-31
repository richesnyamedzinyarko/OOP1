class student:
    grade= 5
    name= 'Riches'
    def introduction (self) :
        print ("Hi I am a student")
    def details (self):
        print("My name is", self.name)
        print("I study in Grade", self.grade)

 #Creating an object
student1= student()
student1.introduction()
student1.details()