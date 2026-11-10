class Pet:
"""A basic pet. Every pet has a name, an age, and some energy."""
def __init__(self, name, age):
self.name = name
self.age = age
self.energy = 3
def speak(self):
return "..."
def play(self):
if self.energy > 0:
self.energy -= 1
return f"{self.name} plays happily! Energy left: {self.energy}"
return f"{self.name} is too tired to play."
def describe(self):
return f"{self.name} is {self.age} years old and says {self.speak()}"
class Dog(Pet):
def speak(self):
return "Woof!"

class Cat(Pet):
def speak(self):
return "Meow."
class Pet:
"""A basic pet. Every pet has a name, an age, and some energy."""
def __init__(self, name, age):
self.name = name
self.age = age
self.energy = 3
def speak(self):
return "..."
def play(self):
if self.energy > 0:
self.energy -= 1
return f"{self.name} plays happily! Energy left: {self.energy}"
return f"{self.name} is too tired to play."
def describe(self):
return f"{self.name} is {self.age} years old and says {self.speak()}"
class Dog(Pet):
def speak(self):
return "Woof!"

class Cat(Pet):
def speak(self):
return "Meow."
