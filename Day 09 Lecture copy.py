class Dog:
    def __init__(self, name, age, breed, tricks = []):
        self.name = name
        self.age = age
        self.breed = breed
        self.tricks = tricks

    def bark(self):
        print(self.name + " says woof!")

    def learn_trick(self, trick):
        self.tricks.append(trick)
        print(self.name + " learned " + trick.lower())

    def print_tricks(self):
        if len(self.tricks) <= 0:
            print(self.name + " doesn't have any tricks.")
        else:
            tricks = self.name + " knows "
            for trick in self.tricks:
                tricks += trick.lower() + ", "
            print(tricks)

dog1 = Dog("Apollo", 1, "Rottweiler")
dog1.bark()

dog2 = Dog("Essie", 100, "Pitbull",["Sit", "Stay"])
dog2.bark()

dog3 = Dog("Snowbear", 1000, "American Eskimo")
dog3.bark()

dog1.print_tricks()
dog2.print_tricks()
dog1.learn_trick("Sit")
dog3.print_tricks()