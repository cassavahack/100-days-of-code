class Dog:
    """An attempt to model a real dog"""

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def sit(self):
        print(f"{self.name} is sitting")

    def roll(self):
        print(f"{self.name} rolled over!")




my_dog = Dog("Fetita", 6)
your_dog = Dog("Joey",4)

print(f"my dogs name is {my_dog.name}")
print(f"my dogs age is {my_dog.age}")

my_dog.sit()
my_dog.roll()

print(f"\n your dogs name is {your_dog.name}")
print(f"\n your dogs age is {your_dog.age}")
your_dog.sit()
your_dog.roll()