#AbstractFactory

class Dog:
    
    """A simple dog class"""
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"
    
class Cat: 
    """A simple cat class"""
    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"

class DogFactory: 
    """Concrete Factory"""
    def get_pet(self):
        """Returns a Dog object"""
        return Dog()
    
    def get_food(self):
        """Returns a Dog food Object"""
        return "Pedigree"
    
class CatFactory: 
    """Concrete Factory"""
    def get_pet(self):
        """Returns a Cat object"""
        return Cat()
    
    def get_food(self):
        """Returns a cat food Object"""
        return "Whiskas"
    
class PetStore:
    """PetStore houses our Abstract Factory"""
    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utily method to display the details of the objects returned by the Factory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print("Our pet is '{}'".format(pet))
        print("Our pet say hello by '{}'".format(pet.speak()))
        print("It's food is '{}'".format(pet_food))

    def set_factory(self, pet_factory):
        self._pet_factory = pet_factory

#Create a Concrete Factory
dogfactory = DogFactory()
#Create a pet store housing our abstract factory
shop = PetStore(dogfactory)
shop.show_pet()
#Create a Cat Factory
catfactory = CatFactory()
shop.set_factory(catfactory)
shop.show_pet()
