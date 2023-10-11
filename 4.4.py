# Придумать класс самостоятельно, реализовать в нем методы экземпляра класса, статические методы, методы класса
class Animal:
    count: int = 0

    def __init__(self, name: str, sound: str, age: int):
        self.name = name
        self.sound = sound
        self.age = age
        Animal.count += 1

    def getname(self):
        return self.name

    def getsound(self):
        return self.sound

    @staticmethod
    def printcount():
        print("Count = ", Animal.count)

    @classmethod
    def getcount(cls):
        # print("Class count = ", cls.count)
        return cls.count


cat1 = Animal('cat', 'meow', 2)
cat2 = Animal('cat 2', 'meow-meow', 5)
Animal.printcount()
dog = Animal('dog', "gav", 9)
print("Cat 1 name:", cat1.getname(), f'({cat1.name})')
print("Dog sound:", dog.getsound())
cat1.name = 'cat 1'
print("New cat 1 name:", cat1.getname())
print("Animal count (class):", Animal.getcount())
print("Animal count (dog)", dog.getcount())
cat2.printcount()
Animal.printcount()
