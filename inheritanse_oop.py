class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and am speaking ')

    def speak(self):
        print('I donT know yet')

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and am {self.color} color ')

class Dog(Pet):
    def speak(self):
        print('Bark')

c1 = Pet('Murka', 8)
c1.show()
c1.speak()
d1 = Dog('Tomka',12)
d1.show()
d1.speak()
c2= Cat('bb', 3, 'green')
c2.speak()
c2.show()

