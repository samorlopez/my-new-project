n = 10
item = "Chapter 1"

print("There are {} sections in {}.".format(n, item))
print("There are {0} sections in {0}.".format(item, n))
print(f"There are {n} sections in {item}.")

def sayagain(s, n=2):
    return s*n

print(sayagain("Hello"))
print(sayagain("Hello", 3))
print()

class Animal:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def info(self):
        print(self.get_name())

class Pet(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def get_age(self):
        return self.age
    def info(self):
        print(self.get_name() + " is " + str(self.get_age()) + " years old.")

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def get_breed(self):
        return self.breed
    def info(self):
        print(f"{self.get_name()} is a {self.get_breed()} and is {self.get_age()} years old.")

class TrainedDog(Dog):
    def __init__(self, name, age, breed, tricks=[]):
        super().__init__(name, age, breed)
        self.tricks = tricks
    def get_tricks(self):
        return self.tricks
    def bark(self):
        if "Bark" in self.tricks:
            print(f"{self.name} is barking.")
        else:
            print (f"{self.name} doesn't know how to bark.")
    def info(self):
        super().info()
        if len(self.tricks) != 0:
            print(f"{self.get_name()} knows how to {self.get_tricks()}")
        else:
            print(f"{self.get_name()} doesn't know any tricks")

if __name__ == "__main__":
    Animal1 = Animal("Tiger")
    Animal1.info()

    Pet1 = Pet("Snowbear", 100000)
    Pet1.info()

    Dog1 = Dog("Essie", 50, "Pitbull")
    Dog1.info()

    TrainedDog1 = TrainedDog("Apollo", 1, "Rottweiler", ["Sit", "Stay", "Bark"])
    TrainedDog1.info()
    TrainedDog1.bark()

    TrainedDog2 = TrainedDog("Beau", 2, "Golden Retriever", ["Shit on the floor"])
    TrainedDog2.info()
    TrainedDog2.bark()

    TrainedDog3 = TrainedDog("Dubs", 3, "Husky")
    TrainedDog3.info()
