class Animal:
    """
    A class used to represent an animal
    """

    zoo_name = "Hayaton"

    def __init__(self, name="", hunger=0):
        """
        :param name: Animal name
        :param hunger: animal hunger level
        :type name: str
        :type hunger: int
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        # Check hunger level
        return True if self._hunger > 0 else False

    def feed(self):
        self._hunger -= 1

    def talk(self, content):
        """
        :param content(str): text for each animal
        """
        print(content)


class Dog(Animal):

    def talk(self):
        super().talk("woof woof")   # using super to import from Animal class

    def fetch_stick(self):  # Special attribute
        print("There you go, sir!")


class Cat(Animal):

    def talk(self):
        super().talk("meow")

    def chase_laser(self):  # Special attribute
        print("Meeeeow")


class Skunk(Animal):

    # Section 7 - unique attribute for the Skunk smell count
    def __init__(self, name="", hunger=0, count=0):
        """
        :param name: Animal name
        :param hunger: animal hunger level
        :param: count: Skunk smell count
        :type name: str
        :type hunger: int
        :type count: int
        """
        Animal.__init__(self, name, hunger) # Import Animal init method
        self._stink_count = count

    def talk(self):
        super().talk("tsssss")

    def stink(self):    # Special attribute
        print("Dear lord!")


class Unicorn(Animal):

    def talk(self):
        super().talk("Good day, darling")

    def sing(self): # Special attribute
        print("I’m not your toy...")

class Dragon(Animal):

    # Section 7 - unique attribute for the Dragon color
    def __init__(self, name="", hunger=0, color="Green"):
        """
        :param name: Animal name
        :param hunger: animal hunger level
        :param: color: Dragon color
        :type name: str
        :type hunger: int
        :type color: str
        """
        Animal.__init__(self, name, hunger) # Import Animal init method
        self._color = color

    def talk(self):
        super().talk("Raaaawr")

    def breath_fire(self):  # Special attribute
        print("$@#$#@$")


def main():
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky",)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)

    zoo_lst = [brownie, zelda, stinky, keith, lizzy]

    # Section 8 - Create new animals
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_jr = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    McFly = Dragon("McFly", 80)
    zoo_lst.extend([doggo, kitty, stinky_jr, clair, McFly]) # Add new animal to the zoo list

    hungry_animals = []

    for animal in zoo_lst:
        ClassType_and_AnimalName = type(animal).__name__ + " " + animal.get_name()
        while animal.is_hungry():   # If hunger level is bigger than 0
            animal.feed()   # Reduce hunger level by one
            hungry_animals.append(ClassType_and_AnimalName)
        # Section 5 - Print each animal specific talk method 
        print(ClassType_and_AnimalName)
        animal.talk()

        # Section 6 - Print each animal uniqe caption method
        if isinstance(animal ,Dog):
            animal.fetch_stick()
        elif isinstance(animal ,Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

        print(" ")  # Empty line

    # Section 4 - Print only the hungry animals
    hungry_animals = "\n".join(dict.fromkeys(hungry_animals))   # Remove duplicate animals from list
    print("* Hungry Animals: *\n" + hungry_animals)

    # Section 9 - Print the zoo name
    print("\n" + "The zoo name is:", Animal.zoo_name)


if __name__ == '__main__':
    main()