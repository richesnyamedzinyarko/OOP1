class parrot:
    species = "Bird"

    #Init Method 
    def __init__(self, name, age):
        self.name=name 
        self.age = age

        #Creating Object

blue = parrot ("Blu", 10)
Woo = parrot ("Woo" , 15)

        #Accesing the class attribute
print('Blue is a {}'. format (blue.species))
print('Woo is a {}'. format (Woo.species))

        #access the instance variables
print ('{} is {} years old'.format (Woo.name, Woo.species))
print ('{} is {} years old'.format (blue.name, blue.species))