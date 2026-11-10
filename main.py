from pets import Dog, Cat
def main():
shelter = [Dog("Bantay", 3), Cat("Mingming", 2)]
for pet in shelter:
print(pet.describe())
print(pet.play())
print("---")
if __name__ == "__main__":
main()
Student B's change (Part 2)
Add this to the bottom of pets.py. It shows a subclass with its own extra attribute, using super() to
reuse the parent's code:
class Bird(Pet):
def __init__(self, name, age, can_fly=True):
super().__init__(name, age)
self.can_fly = can_fly
self.energy = 5
def speak(self):
return "Tweet!"
def describe(self):
flying = "can fly" if self.can_fly else "cannot fly"
return super().describe() + f" and {flying}."
In main.py, change the first line and the shelter line to:
from pets import Dog, Cat, Bird
shelter = [Dog("Bantay", 3), Cat("Mingming", 2), Bird("Tweety", 1)]
