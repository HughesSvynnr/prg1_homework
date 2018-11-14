


class Dog:
    def __init__(self,initial_name,age=0):
        self.age=age
        self.name = initial_name
        pass

    def speak(self):
        print(self.name + " says borf")

    
    def change_name(self,newname):
        self.name= newname

    def calculate_dog_years(self):
        return self.age * 7

    def celebrate_birthday(self):
        self.age +=1
        print("Happy birthday "+ self.name)





fido = Dog("fido",3)
fido.speak()
fido.change_name("Remmy")
fido.speak()
rex = Dog("rex",0)
rex.change_name("Boxiplenty")
rex.speak()
fido.celebrate_birthday()
print(fido.age)
rex.celebrate_birthday()
print(rex.age)
thor = Dog("Thor",11)
thor.celebrate_birthday()
print(thor.age)