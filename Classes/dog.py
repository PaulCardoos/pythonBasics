#this is a class that describes a dog
#a class is a user defined data structure that hold it own data and member functions


class Dog: 
    #each class is required to have a constructor to initialize an object in your class
    def __init__(self, breed, color, age):
        #these are the classes atributes (variables that live in the class)
        self.breed = breed
        self.color = color 
        self.age = age

    #this is a member function and is to be called on an instance of the class
    def bark(self):
        return print("Woof Woof")

#here we initialize an object of this class and define the attributes
doggie = Dog("schnauzer", "gray", 2)

#each object can call a method defined in the class
doggie.bark()





