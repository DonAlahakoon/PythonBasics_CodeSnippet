                #OOP

class Book:
        #defining a constructor
    def __init__(self,title,author):
        self.title = title
        self.author = author

        # Getters and Setters(Special way i.e using property)
                    #any time user access 'title' will automatically go through the getter and setter
    @property
    def title(self): #creating a property title function for the title attr,
        print("Getting title")
        return self._title  #'_' is used to express it is private
    @title.setter
    def title(self,value):
        print("Setting title")
        self._title = value
    @title.deleter
    def title(self):
        del self._title

    def read_book(self):
        print("Reading ",self.title,"by",self.author)

# creating an object from Book class
b1= Book("Harry Potter","JK Roling")
print("\n")
b1.read_book()
print("\n")
print(b1.title)

print("\n\n")


            #Inheritance

class Chef:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def make_chicken(self):
        print("The chef makes chicken")
    def make_special_diah(self):
        print("The chef bbq ribs")

class ItalianChef(Chef): # Italian cheff class inheriting chef class

    def __init__(self,name,age,ctry_of_origin):
        self.ctry_of_origin = ctry_of_origin
        super(ItalianChef,self).__init__(name,age)

    def make_pasta(self):
        print("The chef makes pasta")
    def make_special_diah(self):
        print("The chef makes chicken parm")



myChef = Chef("Gordan Ramsy",60)
myItalianChef  = ItalianChef("Bonjourno",46,"Italy")

myChef.make_chicken()
myChef.make_special_diah()

myItalianChef.make_chicken()
myItalianChef.make_special_diah()
print(myItalianChef.age);
print("\n")


        #Exception handling

try:
    answer = 10 / int(input("Enter a number: "))
    print(answer)
except ZeroDivisionError as e:
    print(e) # print the error if zero input by the user
except:
    print("Caught an error")

### How to use python interpreter
#   type "py" or "python" then python commands can be executed through command prompt