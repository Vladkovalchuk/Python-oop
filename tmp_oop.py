
class Dog:
    """ dirty animal """
    def meow(self):
        """ meow """
        return "meow"
    def bark(self):
        """ bark"""
        print('bark')

boris = Dog()
print(type(boris))
boris.bark()
print(boris.meow())