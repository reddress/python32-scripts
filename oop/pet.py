class pet:
    number_of_legs = 0

    def sleep(self):
        print("zzz")

    def count_legs(self):
        print("I have", self.number_of_legs, "legs")

class dog(pet):
    def bark(self):
        print("Woof")
    def sleep(self):
        print("ZZZZZ")


doug = pet()

amy = pet()

doug.number_of_legs = 4

print("amy has", amy.number_of_legs, "legs")

snoop = dog()
snoop.bark()
